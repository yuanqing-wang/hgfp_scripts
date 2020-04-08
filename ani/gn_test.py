import hgfp
import torch
import dgl
import numpy as np
import copy
import random
import math


ds_tr = hgfp.data.ani.df.topology_batched(10, mm=True)
ds_te = list(hgfp.data.ani.df.topology_batched(120, mm=True))[100:]

mean_and_std_dict = torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/norm_dict')

mean_and_std_dict['angle']['eq']['mean'] = mean_and_std_dict['angle']['eq']['mean'] / 180 * math.pi

mean_and_std_dict['angle']['eq']['std'] = mean_and_std_dict['angle']['eq']['std'] / 180 * math.pi

net = hgfp.models.gcn_with_combine_readout.Net(
    [512, 'tanh', 512, 'tanh', 512, 'tanh'])

net.load_state_dict(
    torch.load('model.ds'),
    strict=False)

norm, unnorm = hgfp.data.utils.get_norm_fn_log_normal(mean_and_std_dict)

def train(g_, x, u):
    g = copy.deepcopy(g_)

    g_ = dgl.batch_hetero([g_ for _ in range(u.shape[0])])

    g = net(g, return_graph=True)

    # g.nodes['bond'].data['k'] = k
    # g.nodes['bond'].data['eq'] = eq

    # g = unnorm(g)

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

    u_hat = torch.sum(
            torch.cat(
            [
                g.nodes['mol'].data['u' + term][:, None] for term in [
                    'bond', 'angle'# , 'torsion', 'one_four', 'nonbonded'# , '0'
            ]],
            dim=1),
        dim=1)

    return u, u_hat, g_, g




for term in ['bond', 'angle']:
    for param in ['k', 'eq']:
        for ds_p in ['tr', 'te']:
            for nt_p in ['true', 'pred']:
                exec(term + param + ds_p + nt_p + '=[]')



for ds_p in ['tr', 'te']:
    for g_, x, u, g_h in globals()['ds_' + ds_p]:
        u, u_hat, g_, g = train(g_, x, u)
        
        print(u)
        print(u_hat)

        for term in ['bond', 'angle']:
            for param in ['k', 'eq']:
                globals()[term + param + ds_p + 'true'].append(
                    g_.nodes[term].data[param])
                
                globals()[term + param + ds_p + 'pred'].append(
                    g.nodes[term].data[param])

    

for term in ['bond', 'angle']:
    for param in ['k', 'eq']:
        for ds_p in ['tr', 'te']:
            for nt_p in ['true', 'pred']:
                x = torch.cat(
                    globals()[term + param + ds_p + nt_p]).detach().numpy()

                np.save(term + '_' + param + '_' + ds_p + '_' + nt_p + '.npy', x)
