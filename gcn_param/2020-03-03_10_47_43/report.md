2020-03-03_10_47_43
===========================
# Model Summary
model=gcn_with_combine_readout
config=['128', 'relu', '128']
hetero=False
data=qm9
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
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
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
    (fr_angle_0): Linear(in_features=384, out_features=128, bias=True)
    (fr_mol): Sequential(
      (0): Linear(in_features=128, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d2): GN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
)
# Time Used 
1.34

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.02         |229424702527609770008839820527867527168.00|
|VALIDATION    |-0.21         |0.05          |
|TEST          |-0.16         |0.05          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-4.16         |9793960926944290942634317316096.00|
|VALIDATION    |-0.17         |0.08          |
|TEST          |-0.01         |0.09          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |726.29        |
|VALIDATION    |-0.03         |117.42        |
|TEST          |0.00          |181.43        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.55         |529313900941786756205772800.00|
|VALIDATION    |-0.91         |0.16          |
|TEST          |-0.47         |0.14          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |91.33         |
|VALIDATION    |-0.88         |337.51        |
|TEST          |-4.02         |49.87         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |71.18         |
|VALIDATION    |-2.51         |69.28         |
|TEST          |-5.93         |57.64         |

