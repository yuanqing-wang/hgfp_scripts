2020-03-03_10_58_46
===========================
# Model Summary
model=gcn_with_combine_readout
config=['128', 'relu', '128', 'relu', '128', 'relu']
hetero=False
data=parm_at_Frosst
batch_size=16
n_epochs=100
size=100
optimizer=Adam
learning_rate=1e-05
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=117, out_features=128, bias=True)
    (1): Tanh()
  )
  (d0): GN(
    (gn): GraphConv(in=128, out=128, normalization=True, activation=None)
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
    (fr_mol): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d2): GN(
    (gn): GraphConv(in=128, out=128, normalization=True, activation=None)
  )
  (d4): GN(
    (gn): GraphConv(in=128, out=128, normalization=True, activation=None)
  )
)
# Time Used 
17.64

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.03          |0.06          |
|VALIDATION    |0.02          |0.06          |
|TEST          |0.03          |0.06          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.08          |0.28          |
|VALIDATION    |0.10          |0.26          |
|TEST          |0.08          |0.28          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.08          |147.27        |
|VALIDATION    |0.07          |152.11        |
|TEST          |0.08          |148.31        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.08          |0.18          |
|VALIDATION    |0.08          |0.19          |
|TEST          |0.09          |0.17          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.29          |20.98         |
|VALIDATION    |0.06          |42.75         |
|TEST          |0.28          |20.93         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.12          |7.02          |
|VALIDATION    |0.08          |7.06          |
|TEST          |0.15          |5.80          |

