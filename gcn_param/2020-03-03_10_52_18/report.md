2020-03-03_10_52_18
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
2.05

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |32777119893488682254472882285445120.00|
|VALIDATION    |0.04          |0.07          |
|TEST          |-0.01         |0.06          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.51         |12993071004234304.00|
|VALIDATION    |0.08          |0.27          |
|TEST          |0.06          |0.29          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |756.72        |
|VALIDATION    |-0.01         |160.39        |
|TEST          |-0.11         |159.59        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.59         |4255411271378153766912.00|
|VALIDATION    |-1.78         |0.34          |
|TEST          |-2.24         |0.31          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |127.61        |
|VALIDATION    |-0.27         |28.96         |
|TEST          |-0.19         |26.91         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |132.59        |
|VALIDATION    |-0.08         |9.53          |
|TEST          |-0.26         |6.91          |

