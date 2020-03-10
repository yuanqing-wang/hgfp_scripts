2020-03-10-185127570064
===========================
# Model Summary
model=gcn_with_combine_readout
config=['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1']
hetero=True
data=ani
batch_size=16
n_epochs=30
size=10000
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_in_buffer=12
cache=True
n_batches_te=10
n_batches_vl=10
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=117, out_features=128, bias=True)
    (1): Tanh()
  )
  (d0): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=128, out_features=128, bias=True)
      (fc_neigh): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle_0): Linear(in_features=384, out_features=128, bias=True)
    (fr_torsion_0): Linear(in_features=512, out_features=128, bias=True)
    (fr_bond_0): Linear(in_features=256, out_features=128, bias=True)
    (fr_mol): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d3): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=128, out_features=128, bias=True)
      (fc_neigh): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d6): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=128, out_features=128, bias=True)
      (fc_neigh): Linear(in_features=128, out_features=128, bias=True)
    )
  )
)
# Time Used 
2851.38

# Dataset Size
Training samples: 
Training: 10177, Validation: 161, Test: 161
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.01          |9.90          |
|VALIDATION    |-1366.50      |8.14          |
|TEST          |-1390.73      |8.21          |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>