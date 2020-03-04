2020-03-03_16_19_11
===========================
# Model Summary
model=walk_recurrent
config=['128', '0.1', 'relu', '128', '0.1', 'relu', '128', '0.1', 'relu']
hetero=False
data=parm_at_Frosst
batch_size=16
n_epochs=100
size=1000
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=10
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
3228.81

# Dataset Size
Training samples: 
Training: 816, Validation: 160, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |1.00          |0.00          |
|VALIDATION    |1.00          |0.00          |
|TEST          |1.00          |0.00          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |1.00          |0.02          |
|VALIDATION    |1.00          |0.02          |
|TEST          |0.99          |0.03          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.96          |28.86         |
|VALIDATION    |0.96          |29.14         |
|TEST          |0.98          |22.85         |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |0.01          |
|VALIDATION    |0.99          |0.01          |
|TEST          |1.00          |0.01          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |2.21          |
|VALIDATION    |0.99          |2.21          |
|TEST          |0.99          |2.76          |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.97          |1.26          |
|VALIDATION    |0.97          |1.29          |
|TEST          |0.97          |1.37          |

