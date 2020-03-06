2020-03-03_15_33_48
===========================
# Model Summary
model=walk_recurrent
config=['128', 'relu', '128']
hetero=False
data=parm_at_Frosst
batch_size=2
n_epochs=30
size=10
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
  (d2): WRGN(
    (gru): GRU(128, 128, batch_first=True)
    (d): Sequential(
      (0): Linear(in_features=512, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=128, bias=True)
    )
  )
)
# Time Used 
6.35

# Dataset Size
Training samples: 
Training: 6, Validation: 2, Test: 2
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.38          |0.06          |
|VALIDATION    |0.42          |0.04          |
|TEST          |0.47          |0.05          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.44          |0.21          |
|VALIDATION    |0.46          |0.22          |
|TEST          |0.53          |0.18          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.11          |147.68        |
|VALIDATION    |0.09          |143.83        |
|TEST          |-0.24         |178.76        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.07          |0.18          |
|VALIDATION    |0.05          |0.16          |
|TEST          |0.08          |0.22          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.21          |24.15         |
|VALIDATION    |0.21          |22.28         |
|TEST          |-0.01         |25.05         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.04          |11.79         |
|VALIDATION    |0.08          |8.87          |
|TEST          |-0.48         |9.83          |

