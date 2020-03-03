2020-03-03_10_50_56
===========================
# Model Summary
model=gcn_with_combine_readout
config=['128', 'relu', '128']
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
)
# Time Used 
3.24

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |33120069923229257465124612032430080.00|
|VALIDATION    |0.08          |0.06          |
|TEST          |0.13          |0.06          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.01         |19938062841049668.00|
|VALIDATION    |-0.02         |0.26          |
|TEST          |-0.03         |0.25          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |800.86        |
|VALIDATION    |-0.01         |149.68        |
|TEST          |-0.02         |156.05        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.41         |3649491010258759843840.00|
|VALIDATION    |-0.79         |0.23          |
|TEST          |-0.91         |0.26          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |110.37        |
|VALIDATION    |-0.23         |28.35         |
|TEST          |-0.25         |27.34         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |124.60        |
|VALIDATION    |-1.96         |13.93         |
|TEST          |-2.06         |13.00         |

