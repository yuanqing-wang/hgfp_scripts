#!/usr/bin/env python
# coding: utf-8

# In[3]:


import hgfp
import torch
import dgl
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from matplotlib import pyplot as plt

import tempfile
import os
import shutil


from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from openeye import oechem
from openforcefield.topology import Molecule
from openforcefield.topology import Topology
from openforcefield.typing.engines.smirnoff import ForceField
FF = ForceField('test_forcefields/smirnoff99Frosst.offxml')
from dgl.nn import pytorch as dgl_pytorch


# In[2]:


import xml.etree.ElementTree as ET
tree = ET.parse('/Users/wangy1/anaconda3/envs/hgfp/lib/python3.7/site-packages/openmmforcefields/ffxml/amber/gaff/ffxml/gaff-2.11.xml')
root = tree.getroot()
nb = root.getchildren()[-1]
atom_types = [atom.get('type') for atom in nb.findall('Atom')]
str_2_idx = dict(zip(atom_types, range(len(atom_types))))
idx_2_str = dict(zip(range(len(atom_types)), atom_types))
print(idx_2_str)


# In[17]:


ds = []

from openeye import oechem
ifs = oechem.oemolistream()
ifs.open('/Users/wangy1/Documents/hgfp_scripts/gcn_param/parm_at_Frosst/zinc.sdf')

idx = 0
for molecule in ifs.GetOEMols():
    if idx > 2000:
        break
    try:
        g = hgfp.graph.from_oemol(molecule)
        g = hgfp.heterograph.from_graph(g)

        molecule = Molecule.from_openeye(molecule)
        print(molecule.to_smiles())
        from openmmforcefields.generators import GAFFTemplateGenerator
        gaff = GAFFTemplateGenerator(molecules=molecule)

        # Create temporary directory for running antechamber

        tmpdir = tempfile.mkdtemp()
        prefix = 'molecule'
        input_sdf_filename = os.path.join(tmpdir, prefix + '.sdf')
        gaff_mol2_filename = os.path.join(tmpdir, prefix + '.gaff.mol2')
        frcmod_filename = os.path.join(tmpdir, prefix + '.frcmod')

        # Write MDL SDF file for input into antechamber
        molecule.to_file(input_sdf_filename, file_format='sdf')

        gaff._run_antechamber(molecule_filename=input_sdf_filename, input_format='mdl',
                gaff_mol2_filename=gaff_mol2_filename, frcmod_filename=frcmod_filename)
        gaff._read_gaff_atom_types_from_mol2(gaff_mol2_filename, molecule)
        gaff_types = [atom.gaff_type for atom in molecule.atoms]
        shutil.rmtree(tmpdir)

        g.nodes['atom'].data['type'] = torch.tensor(
            [str_2_idx[type_str] for type_str in gaff_types])

        ds.append(g)
        idx += 1
    except:
        pass
    


# In[18]:


print(ds)


# In[19]:


ds_tr = ds[:1000]
ds_te = ds[1000:]
g_tr = dgl.batch_hetero(ds_tr)
g_te = dgl.batch_hetero(ds_te)


# In[20]:


class GN(torch.nn.Module):
    def __init__(self, model, kwargs):
        super(GN, self).__init__()
        self.gn = model(64, 64, **kwargs)
        
    def forward(self, g, x):
        g_sub = dgl.to_homo(
            g.edge_type_subgraph(['atom_neighbors_atom']))
        x = self.gn(g_sub, x)
        return x        


# In[21]:


class Classifier(torch.nn.Module):
    def __init__(self, in_dim=128, out_dim=256, n_classes=45):
        super(Classifier, self).__init__()
        self.d = torch.nn.Linear(in_dim, out_dim)
        self.c = torch.nn.Linear(out_dim, n_classes)
        
    def forward(self, x):
        y_hat = self.c(
                torch.nn.functional.tanh(
                    self.d(
                        x)))
        
        return y_hat
        


# In[22]:


class Net(torch.nn.Module):
    def __init__(self, model, kwargs):
        super(Net, self).__init__()
        self.f_in = torch.nn.Sequential(
            torch.nn.Linear(117, 64),
            torch.nn.Tanh())
        
        self.gn0 = GN(model, kwargs)
        self.gn1 = GN(model, kwargs)
        self.gn2 = GN(model, kwargs)
        
        self.c = Classifier(64, 64, 97)
        
    def forward(self, g):
        x = g.nodes['atom'].data['h0']
        x = self.f_in(x)
        x = self.gn0(g, x)
        x = torch.nn.functional.tanh(x)
        x = self.gn1(g, x)
        x = torch.nn.functional.tanh(x)
        x = self.gn2(g, x)
        x = self.c(x)
        return x
        


# In[90]:





# In[104]:


plt.clf()
plt.style.use('default')
from matplotlib import rcParams

from matplotlib import cm
cmap = cm.get_cmap('tab20')

fig = plt.figure()
plt.rc('font', family='san-serif', serif='Arial', size=14)
# fig.patch.set_facecolor('white')
ax = fig.add_subplot(111)

idx = 0
for model_name, model in {
        'GraphConv': [dgl_pytorch.conv.GraphConv, {}],
        'TAGConv': [dgl_pytorch.conv.TAGConv, {}],
        'EdgeConv': [dgl_pytorch.conv.EdgeConv, {}],
        'SAGEConv': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'mean'}],
        # 'SAGEConvGCN': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'gcn'}],
        # 'SAGEConvPool': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'pool'}],
        # 'SAGEConvLSTM': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'lstm'}],
        'SGConv': [dgl_pytorch.conv.SGConv, {}],
        # 'GatedGraphConv': [dgl_pytorch.conv.GatedGraphConv, {}],
        # 'ChebConv': [dgl_pytorch.conv.ChebConv, {'k': 3}]
}.items():
    
    print(model_name)
    idx += 1
    net=Net(model[0], model[1])
    opt = torch.optim.Adam(list(net.parameters()), 1e-3)
    loss_fn = torch.nn.CrossEntropyLoss()
    namespace = __import__(__name__)

    for part in ['tr', 'te']:
        exec('accuracy_' + part + '= []')

    for _ in range(500):
        opt.zero_grad()
        y_hat = net(g_tr)
        y = g_tr.nodes['atom'].data['type']
        loss = loss_fn(y_hat, y)
        loss.backward()
        opt.step()

        net.eval()
        for part in ['tr', 'te']:
            y_hat = torch.argmax(net(getattr(namespace, 'g_' + part)), dim=1)
            y = getattr(namespace, 'g_' + part).nodes['atom'].data['type']

            getattr(namespace, 'accuracy_' + part).append(
                1 - np.divide(
                    np.count_nonzero(y_hat - y),
                y_hat.shape[0]))

        net.train()

    
    print(idx)
    ax.plot(accuracy_tr, label=model_name, alpha=0.8, linewidth=3, c=cmap.colors[idx])
    ax.plot(accuracy_te, alpha=0.8, linewidth=3, c=cmap.colors[idx], linestyle='--')
    
    print(accuracy_tr[-1])
    print(accuracy_te[-1])
    # plt.plot(accuracy_te, label='test')
    ax.set_ylim(0, 1)
    ax.legend()
    ax.set_ylabel('Accuracy')
    ax.set_xlabel('Epochs')
    ax.set_facecolor('white')
    
plt.tight_layout()
plt.savefig('.png', dpi=500)


# In[ ]:


net.eval()
from sklearn.metrics import confusion_matrix

y_hat = torch.cat([torch.argmax(net(g), dim=1) for g, y in ds_vl+ds_te], axis=0)
y = torch.cat([torch.argmax(y, dim=1) for g, y in ds_vl+ds_te], axis=0)

print(np.count_nonzero(y - y_hat) / y_hat.shape[0])


# In[12]:


element_to_idx = {b'BR': 0, b'C': 1, b'C2': 2, b'CA': 3, b'CB': 4, b'CC': 5, b'CJ': 6, b'CL': 7, b'CM': 8, b'CP': 9, b'CR': 10, b'CT': 11, b'CW': 12, b'Cstar': 13, b'F': 14, b'H': 15, b'H1': 16, b'H2': 17, b'H3': 18, b'H4': 19, b'H5': 20, b'HA': 21, b'HC': 22, b'HO': 23, b'HP': 24, b'HX': 25, b'I': 26, b'N': 27, b'N2': 28, b'N3': 29, b'NA': 30, b'NB': 31, b'NC': 32, b'NL': 33, b'Nstar': 34, b'Nu': 35, b'O': 36, b'O2': 37, b'OH': 38, b'OS': 39, b'Ou': 40, b'P': 41, b'S': 42, b'SO': 43, b'Su': 44}


# In[13]:


idx_to_element = {v: k.decode("utf-8") for k, v in element_to_idx.items()}


# In[14]:


import pandas as pd
df_cm = pd.DataFrame(confusion_matrix(y, y_hat, labels=list(range(1, 46))),
    [v for k, v in idx_to_element.items()],
    [v for k, v in idx_to_element.items()])


# In[15]:


count_matrix = df_cm.values
wrong_idxs = np.stack(np.where(np.greater(count_matrix, 0)), axis=1)
wrong_idxs = wrong_idxs[wrong_idxs[:, 0] != wrong_idxs[:, 1]]
wrong_count = np.array([count_matrix[idxs[0]][idxs[1]] for idxs in wrong_idxs])
wrong_count_argsort = np.flip(np.argsort(wrong_count))
for idx in wrong_count_argsort:
    print('%s -> %s : %s'%(
        idx_to_element[wrong_idxs[idx][0]],
        idx_to_element[wrong_idxs[idx][1]],
        wrong_count[idx]))


# In[ ]:




