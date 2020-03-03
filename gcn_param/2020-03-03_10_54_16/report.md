2020-03-03_10_54_16
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
2.14

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |23986275311944027336561798213009408.00|
|VALIDATION    |-0.06         |0.07          |
|TEST          |-0.05         |0.07          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.63         |12163780044359674.00|
|VALIDATION    |-0.36         |0.35          |
|TEST          |-0.33         |0.33          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |766.87        |
|VALIDATION    |-0.17         |158.86        |
|TEST          |-0.01         |151.45        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.56         |2213709650309696454656.00|
|VALIDATION    |-0.12         |0.20          |
|TEST          |-0.07         |0.20          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |114.35        |
|VALIDATION    |-0.23         |24.53         |
|TEST          |0.09          |23.27         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |133.73        |
|VALIDATION    |-0.45         |7.83          |
|TEST          |-0.11         |7.96          |

