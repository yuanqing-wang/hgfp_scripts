2020-02-20_14_37_46
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', '0.9', 'relu', '256', '0.9', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
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
      (linear): Linear(in_features=512, out_features=256, bias=True)
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
56.99

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.47          |0.03          |
|VALIDATION    |0.37          |0.04          |
|TEST          |0.25          |0.04          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.49          |0.06          |
|VALIDATION    |0.45          |0.06          |
|TEST          |0.21          |0.08          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.66          |103.39        |
|VALIDATION    |0.53          |97.52         |
|TEST          |0.40          |144.20        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.47          |0.09          |
|VALIDATION    |0.32          |0.10          |
|TEST          |0.32          |0.11          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.51          |120.60        |
|VALIDATION    |0.21          |95.86         |
|TEST          |-5.61         |61.38         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.60          |17.85         |
|VALIDATION    |0.36          |25.14         |
|TEST          |0.56          |19.61         |

