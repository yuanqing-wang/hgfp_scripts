2020-02-20_12_48_16
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=False
data=QM9
batch_size=16
n_epochs=100
size=100
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=10, out_features=32, bias=True)
    (1): Tanh()
  )
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=256, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
)
# Time Used 
15.93

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.81          |0.02          |
|VALIDATION    |0.56          |0.03          |
|TEST          |0.69          |0.03          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |0.01          |
|VALIDATION    |0.96          |0.02          |
|TEST          |0.96          |0.02          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.85          |67.27         |
|VALIDATION    |-0.09         |172.74        |
|TEST          |0.19          |155.38        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.75          |0.06          |
|VALIDATION    |0.29          |0.10          |
|TEST          |0.48          |0.09          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.80          |70.77         |
|VALIDATION    |0.82          |56.24         |
|TEST          |-0.05         |182.36        |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.77          |13.75         |
|VALIDATION    |0.53          |19.91         |
|TEST          |0.64          |19.12         |

