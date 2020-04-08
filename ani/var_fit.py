import hgfp
import torch
import dgl
import numpy as np
import copy

ds = hgfp.data.ani.df.topology_batched(0, mm=True)

loss_fn = torch.nn.functional.mse_loss

for g_, u in ds:
    # k = torch.tensor(np.load('k.npy'))
    # eq = torch.tensor(np.load('eq.npy'))
    
    k = torch.nn.Parameter(torch.zeros_like(dgl.unbatch_hetero(g_)[0].nodes['bond'].data['k']))
    eq = torch.nn.Parameter(torch.zeros_like(dgl.unbatch_hetero(g_)[0].nodes['bond'].data['eq']))
    
    opt = torch.optim.Adam([k, eq], 1e-1)

    for _ in range(100):
        g = copy.deepcopy(g_)
        g.nodes['bond'].data['k'] = k.repeat(g.batch_size)
        g.nodes['bond'].data['eq'] = eq.repeat(g.batch_size)

        g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
            g)

        g = hgfp.mm.energy_in_heterograph.u(g)

        # g = unnorm(g)


        print(g.nodes['mol'].data['ubond'])

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

        loss = loss_fn(u, u_hat)
        print(loss)
        opt.zero_grad()
        loss.backward()
        opt.step()

from matplotlib import pyplot as plt

plt.scatter(u.detach().numpy(), u_hat.detach().numpy())

plt.savefig('_img.png')
    
