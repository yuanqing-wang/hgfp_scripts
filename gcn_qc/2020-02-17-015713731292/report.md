2020-02-17-015713731292
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=True
data=qc_archive
batch_size=32
n_epochs=100
size=100
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_in_buffer=12
cache=True
n_batches_te=3
n_batches_vl=3
report=True

Net(
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=10, out_features=256, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
)
# Time Used 
8145.25

# Dataset Size
Training samples: 
Training: 2689, Validation: 97, Test: 97
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.46         |304.81        |
|VALIDATION    |-1.82         |320.00        |
|TEST          |-1.06         |284.20        |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>