2020-03-03_10_56_54
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', '32']
hetero=False
data=parm_at_Frosst
batch_size=16
n_epochs=30
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
    (gn): GraphConv(in=128, out=32, normalization=True, activation=None)
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=32, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=32, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=32, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=32, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle_0): Linear(in_features=96, out_features=32, bias=True)
    (fr_mol): Sequential(
      (0): Linear(in_features=32, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d1): GN(
    (gn): GraphConv(in=32, out=32, normalization=True, activation=None)
  )
)
# Time Used 
3.43

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.05          |0.06          |
|VALIDATION    |0.06          |0.07          |
|TEST          |0.03          |0.06          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.07          |0.29          |
|VALIDATION    |0.11          |0.25          |
|TEST          |0.10          |0.24          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.04          |150.01        |
|VALIDATION    |0.04          |162.34        |
|TEST          |0.04          |143.20        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.08          |0.18          |
|VALIDATION    |0.08          |0.18          |
|TEST          |0.07          |0.17          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.00         |24.88         |
|VALIDATION    |0.00          |24.76         |
|TEST          |0.00          |43.93         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.00         |7.03          |
|VALIDATION    |-0.01         |8.87          |
|TEST          |-0.01         |7.00          |

