2020-03-03_15_39_34
===========================
# Model Summary
model=walk_recurrent
config=['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1', 'relu']
hetero=False
data=parm_at_Frosst
batch_size=16
n_epochs=30
size=100
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=117, out_features=128, bias=True)
    (1): Tanh()
  )
  (d0): WRGN(
    (gru): GRU(128, 128, batch_first=True)
    (d): Sequential(
      (0): Linear(in_features=512, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=128, bias=True)
    )
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
  )
  (d3): WRGN(
    (gru): GRU(128, 128, batch_first=True)
    (d): Sequential(
      (0): Linear(in_features=512, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d6): WRGN(
    (gru): GRU(128, 128, batch_first=True)
    (d): Sequential(
      (0): Linear(in_features=512, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=128, bias=True)
    )
  )
)
# Time Used 
80.39

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.95          |0.01          |
|VALIDATION    |0.92          |0.02          |
|TEST          |0.93          |0.02          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.96          |0.06          |
|VALIDATION    |0.95          |0.07          |
|TEST          |0.93          |0.07          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.24          |131.40        |
|VALIDATION    |0.26          |130.55        |
|TEST          |0.21          |142.72        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.75          |0.09          |
|VALIDATION    |0.72          |0.10          |
|TEST          |0.69          |0.10          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.50          |21.90         |
|VALIDATION    |0.78          |11.73         |
|TEST          |0.82          |10.40         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.29          |5.98          |
|VALIDATION    |0.23          |6.88          |
|TEST          |0.32          |5.48          |

