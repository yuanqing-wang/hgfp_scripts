2020-02-17_23_49_17
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=False
data=QM9
batch_size=32
n_epochs=10
size=10000
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=30
n_batches_vl=30
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
238.82

# Dataset Size
Training samples: 
Training: 8064, Validation: 960, Test: 960
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-121.70       |0.51          |
|VALIDATION    |-123.38       |0.51          |
|TEST          |-120.78       |0.51          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-321.43       |1.49          |
|VALIDATION    |-317.31       |1.49          |
|TEST          |-319.35       |1.49          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-19.59        |811.72        |
|VALIDATION    |-19.44        |809.14        |
|TEST          |-19.43        |809.44        |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-143.26       |1.17          |
|VALIDATION    |-140.21       |1.16          |
|TEST          |-140.64       |1.17          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.35         |179.31        |
|VALIDATION    |-2.20         |182.94        |
|TEST          |-2.12         |186.05        |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-46.62        |118.25        |
|VALIDATION    |-43.86        |117.97        |
|TEST          |-42.13        |118.39        |

