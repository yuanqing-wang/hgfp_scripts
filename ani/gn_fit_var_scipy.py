import scipy
from scipy import optimize
import hgfp
import torch
import dgl
import numpy as np
import copy
import random
import math
import sys
import mdtraj as md
from dgl import data
from openeye import oechem

def run(config):

    xs = [torch.tensor(
            md.formats.DCDTrajectoryFile('ds_md/%s.dcd' % idx).read()[0])\
                for idx in range(2)]

    # gs, _ = dgl.data.utils.load_graphs('ds_md/gs.bin')
    ifs = oechem.oemolistream()
    mols = []
    
    for idx in range(32):
        ifs.open('ds_md/' + str(idx) + '.sdf')
        mols.append(next(ifs.GetOEGraphMols()))

    gs = [hgfp.data.mm_energy.u(mol, toolkit='openeye', return_graph=True) for mol in mols]
    
    ds = list(zip(gs, xs))

    ds_tr= ds[:1]

    g = ds_tr[0][0]


    mean_and_std_dict = torch.load('/data/chodera/wangyq/hgfp_scripts/gcn_param/2020-03-30_11_41_19/norm_dict')

    mean_and_std_dict['angle']['eq']['mean'] = mean_and_std_dict['angle']['eq']['mean'] / 180 * math.pi

    mean_and_std_dict['angle']['eq']['std'] = mean_and_std_dict['angle']['eq']['std'] / 180 * math.pi

    net = hgfp.models.gcn_with_combine_readout.Net(config)

    norm, unnorm = hgfp.data.utils.get_norm_fn_log_normal(mean_and_std_dict)

    loss_fn = torch.nn.functional.mse_loss

    def train(theta, g_, x):
        
        g = copy.deepcopy(g_)

        g.nodes['bond'].data['k'] = theta[:18]
        g.nodes['bond'].data['eq'] = theta[18:36]
        g.nodes['angle'].data['k'] = theta[36:69]
        g.nodes['angle'].data['eq'] = theta[69:]

        g = unnorm(g)

        g_ = dgl.batch_hetero([g_ for _ in range(x.shape[0])])

        g = dgl.batch_hetero([g for _ in range(x.shape[0])])

        g.nodes['atom'].data['xyz'] = torch.reshape(x, [-1, 3])

        g_.nodes['atom'].data['xyz'] = torch.reshape(x, [-1, 3])

        g = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
            g)

        g_ = hgfp.mm.geometry_in_heterograph.from_heterograph_with_xyz(
            g_)

        g = hgfp.mm.energy_in_heterograph.u(g)
       
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

        return u, u_hat, norm(g_), norm(g)

    for g_, x in ds_tr:
        
        x = x[:64]
       
        def l(theta, g_=g_, x=x):
            theta = torch.Tensor(theta)
            theta.requires_grad = True
            u, u_hat, g_, g = train(theta, g_, x)
            loss = loss_fn(u, u_hat)

            grad = torch.autograd.grad(loss, theta)[0]
            return loss.detach().numpy().astype('float32')# , grad.detach().numpy().astype('float32')

        res = scipy.optimize.minimize(
                l, 
                x0=np.zeros(shape=(102,)), 
                method='L-BFGS-B',
                jac=False,
                options=dict(disp=True, maxiter=1000))
        print(res)
    
if __name__ == '__main__':
    config = sys.argv[1:] 
    run(config)

