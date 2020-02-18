2020-02-18_01_07_55
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=False
data=QM9
batch_size=32
n_epochs=30
size=1000
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
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
56.31

# Dataset Size
Training samples: 
Training: 800, Validation: 96, Test: 96
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.54          |0.03          |
|VALIDATION    |0.51          |0.03          |
|TEST          |0.52          |0.03          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.78          |0.04          |
|VALIDATION    |0.75          |0.04          |
|TEST          |0.79          |0.04          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.58          |119.54        |
|VALIDATION    |0.51          |127.56        |
|TEST          |0.53          |125.60        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.50          |0.08          |
|VALIDATION    |0.47          |0.07          |
|TEST          |0.44          |0.08          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.37          |86.94         |
|VALIDATION    |0.16          |85.79         |
|TEST          |0.12          |63.45         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.44          |14.92         |
|VALIDATION    |0.41          |13.87         |
|TEST          |0.40          |15.59         |

