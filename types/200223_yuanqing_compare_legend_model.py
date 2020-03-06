#!/usr/bin/env python
# coding: utf-8

# In[2]:


import hgfp
import torch
import dgl
import numpy as np
# get_ipython().run_line_magic('matplotlib', 'inline')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from matplotlib import pyplot as plt


# In[3]:


ds = list(hgfp.data.parm_at_Frosst.df.batched(num=100, batch_size=16, use_fp=False))
ds_tr, ds_vl, ds_te = hgfp.data.utils.split(ds, 1, 1)


# In[4]:


from dgl.nn import pytorch as dgl_pytorch


# In[5]:


class GN(torch.nn.Module):
    def __init__(self, model, kwargs):
        super(GN, self).__init__()
        self.gn = model(64, 64, **kwargs)

    def forward(self, g, x):
        g_sub = dgl.to_homo(
            g.edge_type_subgraph(['atom_neighbors_atom']))
        x = self.gn(g_sub, x)
        return x


# In[6]:


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



# In[7]:


class Net(torch.nn.Module):
    def __init__(self, model, kwargs):
        super(Net, self).__init__()
        self.f_in = torch.nn.Sequential(
            torch.nn.Linear(100, 64),
            torch.nn.Tanh())

        self.gn0 = GN(model, kwargs)
        self.gn1 = GN(model, kwargs)
        self.gn2 = GN(model, kwargs)

        self.c = Classifier(64, 64, 45)

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



# In[ ]:


for model_name, model in {
        'GraphConv': [dgl_pytorch.conv.GraphConv, {}],
        'TAGConv': [dgl_pytorch.conv.TAGConv, {}],
        'EdgeConv': [dgl_pytorch.conv.EdgeConv, {}],
        'SAGEConvMean': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'mean'}],
        'SAGEConvGCN': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'gcn'}],
        'SAGEConvPool': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'pool'}],
        'SAGEConvLSTM': [dgl_pytorch.conv.SAGEConv, {'aggregator_type': 'lstm'}],
        'SGConv': [dgl_pytorch.conv.SGConv, {}]}.items():
    print(model_name)
    net=Net(model[0], model[1])
    opt = torch.optim.Adam(list(net.parameters()), 1e-3)
    loss_fn = torch.nn.CrossEntropyLoss()
    namespace = __import__(__name__)

    for part in ['tr', 'vl', 'te']:
        exec('accuracy_' + part + '= []')

    for _ in range(500):
        for g, y in ds_tr:
            opt.zero_grad()
            y_hat = net(g)
            loss = loss_fn(y_hat, torch.where(torch.gt(y, 0))[1])
            loss.backward()
            opt.step()

        net.eval()
        for part in ['tr', 'vl', 'te']:
            y_hat = torch.cat([torch.argmax(net(g), dim=1) for g, y in getattr(
                namespace, 'ds_' + part)], dim=0).detach().numpy()

            y = torch.cat([torch.argmax(y, dim=1) for g, y in getattr(
                namespace, 'ds_' + part)], dim=0).detach().numpy()

            getattr(namespace, 'accuracy_' + part).append(
                1 - np.divide(
                    np.count_nonzero(y_hat - y),
                y_hat.shape[0]))

        net.train()

    plt.style.use('fivethirtyeight')
    plt.figure()
    plt.plot(accuracy_tr, label='training')
    plt.plot(accuracy_vl, label='validation')
    plt.ylim(0, 1)
    plt.legend()
    plt.ylabel('accuracy')
    plt.xlabel('n_epochs')
    plt.title(model_name)
    plt.tight_layout()
    plt.savefig(model_name + '.png', dpi=500)
    plt.close()



# In[ ]:





# In[ ]:
