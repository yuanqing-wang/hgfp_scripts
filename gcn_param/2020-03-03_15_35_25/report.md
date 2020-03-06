2020-03-03_15_35_25
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
80.49

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.00         |0.06          |
|VALIDATION    |-0.00         |0.06          |
|TEST          |-0.00         |0.07          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.00         |0.29          |
|VALIDATION    |-0.01         |0.26          |
|TEST          |-0.00         |0.29          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.62          |93.45         |
|VALIDATION    |0.62          |95.97         |
|TEST          |0.66          |89.92         |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.89          |0.06          |
|VALIDATION    |0.88          |0.06          |
|TEST          |0.91          |0.06          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.54          |20.94         |
|VALIDATION    |0.86          |9.23          |
|TEST          |0.83          |10.46         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.58          |4.95          |
|VALIDATION    |0.54          |4.75          |
|TEST          |0.82          |2.62          |

