import hgfp
import torch
import dgl
import numpy as np
import copy

ds = hgfp.data.ani.df.topology_batched(0, mm=True)
batch_size = 32

net = hgfp.models.gcn_with_combine_readout.Net(
        ['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1', 'relu'])
        
net.load_state_dict(torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/model'))

mean_and_std_dict = torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/norm_dict')

norm, unnorm = hgfp.data.utils.get_norm_fn(mean_and_std_dict)

opt = torch.optim.Adam(net.parameters(), 1e-3)

loss_fn = torch.nn.L1Loss()

for g_, u in ds:
    gs = dgl.unbatch_hetero(g_)
    print(torch.stack([g.nodes['bond'].data['k'] for g in gs]))
    print(torch.stack([g.nodes['bond'].data['eq'] for g in gs]))

    for _ in range(1000):
            g = copy.deepcopy(g_)

            g = net(g, return_graph=True)

            g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
                g)

            g = hgfp.mm.energy_in_heterograph.u(g)

            g = unnorm(g)

            u = torch.sum(
                    torch.cat(
                    [
                        g_.nodes['mol'].data['u' + term][:, None] for term in [
                            'bond', # 'angle', 'torsion', 'one_four', 'nonbonded', '0'
                    ]],
                    dim=1),
                dim=1)


            u_hat = torch.sum(
                    torch.cat(
                    [
                        g.nodes['mol'].data['u' + term][:, None] for term in [
                            'bond', # 'angle', 'torsion', 'one_four', 'nonbonded', '0'
                    ]],
                    dim=1),
                dim=1)

            loss = loss_fn(
                    g_.nodes['bond'].data['eq'],
                    g.nodes['bond'].data['eq']) + loss_fn(
                            g_.nodes['bond'].data['k'],
                            g.nodes['bond'].data['k'])

            print(loss)            
            opt.zero_grad()
            loss.backward()
            opt.step()
        
# np.save('u_hat', u_hat.detach().numpy())
# np.save('u', u.detach().numpy())

np.save('eq', g_.nodes['bond'].data['eq'].detach().numpy())
np.save('eq_hat', g.nodes['bond'].data['eq'].detach().numpy())
np.save('k', g_.nodes['bond'].data['k'].detach().numpy())
np.save('k_hat', g.nodes['bond'].data['k'].detach().numpy())



from matplotlib import pyplot as plt

plt.scatter(u.detach().numpy(), u_hat.detach().numpy())

plt.savefig('img.png')
    
