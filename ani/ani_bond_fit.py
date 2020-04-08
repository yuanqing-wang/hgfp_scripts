import hgfp
import torch
import dgl
import numpy as np
import copy

ds = hgfp.data.ani.df.topology_batched(10, mm=True)
batch_size = 32
net = hgfp.models.gcn_with_combine_readout.Net(
    ['128', 'relu', '0.1', '128', 'relu', '0.1', '128', 'relu', '0.1', '128', 'relu', '0.1', '128', 'relu'])
net.load_state_dict(torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-24_17_34_36/model'))

loss_fn = torch.nn.L1Loss()

for _ in range(1000):
    for g_, u in ds:
            g = copy.deepcopy(g_)

            g = net(g, return_graph=True)

            g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
                g)

            g = hgfp.mm.energy_in_heterograph.u(g)

            # loss = loss_fn(u, u_hat)
            print('k')
            print(g.nodes['bond'].data['k'])
            print(g_.nodes['bond'].data['k'])
            
            print('eq')
            print(g.nodes['bond'].data['eq'])
            print(g_.nodes['bond'].data['eq'])

            loss = loss_fn(g_.nodes['bond'].data['k'], g.nodes['bond'].data['k']
                    ) + loss_fn(
                    g_.nodes['bond'].data['eq'], g.nodes['bond'].data['eq'])

            
            print('u')
            print(g.nodes['mol'].data['ubond'])
            print(g_.nodes['mol'].data['ubond'])
            
            print('loss')
            print(loss)

            opt.zero_grad()
            loss.backward()
            opt.step()
        

torch.save(net.state_dict(), 'bond_model')
