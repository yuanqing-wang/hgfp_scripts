import hgfp
import torch
import dgl
import numpy as np
import copy
import random
import math
import sys

def run(config):
    ds_tr = hgfp.data.ani.df.topology_batched(32, mm=True)

    mean_and_std_dict = torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/norm_dict')

    mean_and_std_dict['angle']['eq']['mean'] = mean_and_std_dict['angle']['eq']['mean'] / 180 * math.pi

    mean_and_std_dict['angle']['eq']['std'] = mean_and_std_dict['angle']['eq']['std'] / 180 * math.pi

    net = hgfp.models.gcn_with_combine_readout.Net(config)

    norm, unnorm = hgfp.data.utils.get_norm_fn_log_normal(mean_and_std_dict)

    opt = torch.optim.Adam(net.parameters(), 1e-4)

    # loss_fn = torch.nn.functional.mse_loss

    loss_fn = torch.nn.L1Loss()

    def train(g_, x, u):

        g = copy.deepcopy(g_)

        g_ = dgl.batch_hetero([g_ for _ in range(u.shape[0])])

        g = net(g, return_graph=True)

        g = unnorm(g)

        g = dgl.batch_hetero([g for _ in range(u.shape[0])])

        g.nodes['atom'].data['xyz'] = torch.reshape(x, [-1, 3])

        g_.nodes['atom'].data['xyz'] = torch.reshape(x, [-1, 3])

        g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
            g)

        g = hgfp.mm.energy_in_heterograph.u(g)

        g_ = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
            g_)
       
        g_ = hgfp.mm.energy_in_heterograph.u(g_)
        
        u = torch.sum(
                torch.cat(
                [
                    g_.nodes['mol'].data['u' + term][:, None] for term in [
                        'bond', 'angle', # 'torsion', 'one_four', 'nonbonded'# , '0'
                ]],
                dim=1),
            dim=1)

        g.nodes['mol'].data['u0'] = g.nodes['mol'].data['u0'][:, 0]

        u_hat = torch.sum(
                torch.cat(
                [
                    g.nodes['mol'].data['u' + term][:, None] for term in [
                        'bond', 'angle', # 'torsion', 'one_four', 'nonbonded', '0'
                ]],
                dim=1),
            dim=1)

        return u, u_hat


    for idx_epoch in range(100):
        loss = 0.
        idx = 0
        for g_, x, u, g_h in ds_tr:
            u, u_hat = train(g_, x, u)
            loss += loss_fn(u, u_hat)
            idx += 1
            if idx == 8:

                print(loss)

                opt.zero_grad()
                loss.backward()
                opt.step()
                idx = 0
                loss =  0.
    net.eval()

    # torch.save(net.state_dict(), 'model.ds')

    ds_te = list(hgfp.data.ani.df.topology_batched(40, mm=True))[32:]

    u_tr = []
    u_hat_tr = []
    u_te = []
    u_hat_te = []

    for g_, x, u, g_h in ds_tr:
        u, u_hat = train(g_, x, u)
        u_tr.append(u)
        u_hat_tr.append(u_hat)

    for g_, x, u, g_h in ds_te:
        u, u_hat = train(g_, x, u)
        u_te.append(u)
        u_hat_te.append(u_hat)

    rmses_tr = np.array([torch.sqrt(torch.mean((u - u_hat) ** 2)).detach().numpy() for u, u_hat in zip(u_tr, u_hat_tr)])
    rmses_te = np.array([torch.sqrt(torch.mean((u - u_hat) ** 2)).detach().numpy() for u, u_hat in zip(u_te, u_hat_te)])

    np.save('rmses_tr', rmses_tr)
    np.save('rmses_te', rmses_te)

    print(rmses_tr)
    print(rmses_te)

    from sklearn.metrics import r2_score

    r2_tr = np.array([r2_score(u.detach().numpy(), u_hat.detach().numpy()) for u, u_hat in zip(u_tr, u_hat_tr)])
    r2_te = np.array([r2_score(u.detach().numpy(), u_hat.detach().numpy()) for u, u_hat in zip(u_te, u_hat_te)])

    print(r2_tr)
    print(r2_te)

if __name__ == '__main__':
    config = sys.argv[1:] 
    run(config)

