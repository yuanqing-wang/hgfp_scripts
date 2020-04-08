import hgfp
import torch
import dgl
import numpy as np
import copy
import random

ds = hgfp.data.ani.df.topology_batched(32, mm=True)

net = hgfp.models.gcn_with_combine_readout.Net(
        ['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1', 'relu'])
        
# net.load_state_dict(torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/model'))

net.load_state_dict(torch.load('model_multi.ds'))

mean_and_std_dict = torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/norm_dict')

norm, unnorm = hgfp.data.utils.get_norm_fn(mean_and_std_dict)

loss_fn = torch.nn.functional.mse_loss

for g_, u in ds:
    g_ = dgl.unbatch_hetero(g_)

    idxs = random.choices(list(range(len(g_))), k=64)
    
    g_ = dgl.batch_hetero(
            [g_[idx] for idx in idxs])
    
    g = copy.deepcopy(g_)
    
    u = u[idxs]

    g = net(g, return_graph=True)

    g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
        g)

    g = hgfp.mm.energy_in_heterograph.u(g)

    g = unnorm(g)

    u = torch.sum(
            torch.cat(
            [
                g_.nodes['mol'].data['u' + term][:, None] for term in [
                    'bond', 'angle', 'torsion', 'one_four', 'nonbonded'# , '0'
            ]],
            dim=1),
        dim=1)


    u_hat = torch.sum(
            torch.cat(
            [
                g.nodes['mol'].data['u' + term][:, None] for term in [
                    'bond', 'angle', 'torsion', 'one_four', 'nonbonded'# , '0'
            ]],
            dim=1),
        dim=1)

    loss = loss_fn(u, u_hat)
    print(loss)
    print(u)
    print(u_hat)
        
# plt.scatter(u.detach().numpy(), u_hat.detach().numpy())

# plt.savefig('img_multi.png')

    
