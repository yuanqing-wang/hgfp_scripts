2020-02-20_14_41_18
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
58.84

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.62          |0.03          |
|VALIDATION    |0.57          |0.03          |
|TEST          |0.52          |0.03          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.85          |0.03          |
|VALIDATION    |0.83          |0.03          |
|TEST          |0.91          |0.02          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.56          |116.48        |
|VALIDATION    |0.41          |136.89        |
|TEST          |0.20          |146.02        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.57          |0.08          |
|VALIDATION    |0.37          |0.10          |
|TEST          |0.28          |0.10          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.57          |107.17        |
|VALIDATION    |0.60          |81.45         |
|TEST          |0.54          |84.94         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.60          |18.64         |
|VALIDATION    |0.53          |20.14         |
|TEST          |0.31          |24.58         |

