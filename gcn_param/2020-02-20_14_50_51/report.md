2020-02-20_14_50_51
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', '0.1', 'relu', '256', '0.1', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=False
data=QM9
batch_size=16
n_epochs=300
size=100
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=10, out_features=128, bias=True)
    (1): Tanh()
  )
  (f_in_e): Sequential(
    (0): Linear(in_features=13, out_features=128, bias=True)
    (1): Tanh()
  )
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d3): GCN(
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
  (d12): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=512, out_features=256, bias=True)
    )
  )
)
# Time Used 
55.91

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.79          |0.02          |
|VALIDATION    |0.80          |0.02          |
|TEST          |0.74          |0.02          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |0.01          |
|VALIDATION    |0.96          |0.02          |
|TEST          |0.97          |0.02          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.83          |69.94         |
|VALIDATION    |0.45          |135.88        |
|TEST          |0.56          |122.63        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.70          |0.07          |
|VALIDATION    |0.70          |0.07          |
|TEST          |0.52          |0.08          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.75          |67.30         |
|VALIDATION    |0.02          |188.77        |
|TEST          |-0.12         |196.30        |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.73          |14.71         |
|VALIDATION    |0.72          |16.43         |
|TEST          |0.66          |18.74         |

