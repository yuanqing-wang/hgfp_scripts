2020-03-03_15_45_18
===========================
# Model Summary
model=walk_recurrent
config=['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1', 'relu']
hetero=False
data=parm_at_Frosst
batch_size=16
n_epochs=100
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
260.00

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |0.00          |
|VALIDATION    |0.99          |0.00          |
|TEST          |1.00          |0.00          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |0.03          |
|VALIDATION    |0.98          |0.04          |
|TEST          |0.99          |0.03          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.86          |56.56         |
|VALIDATION    |0.85          |58.76         |
|TEST          |0.83          |66.30         |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.98          |0.03          |
|VALIDATION    |0.98          |0.03          |
|TEST          |0.98          |0.03          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.96          |4.65          |
|VALIDATION    |0.24          |38.23         |
|TEST          |0.95          |5.28          |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.96          |1.56          |
|VALIDATION    |0.77          |3.42          |
|TEST          |0.89          |2.29          |

