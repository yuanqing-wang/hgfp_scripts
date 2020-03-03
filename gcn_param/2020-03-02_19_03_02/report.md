2020-03-02_19_03_02
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', 'relu', '32', 'relu', '32', 'relu']
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
  (d0): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=128, out_features=32, bias=True)
      (fc_neigh): Linear(in_features=128, out_features=32, bias=True)
    )
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
  (d2): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=32, out_features=32, bias=True)
      (fc_neigh): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d4): GN(
    (gn): SAGEConv(
      (feat_drop): Dropout(p=0.0, inplace=False)
      (fc_self): Linear(in_features=32, out_features=32, bias=True)
      (fc_neigh): Linear(in_features=32, out_features=32, bias=True)
    )
  )
)
# Time Used 
2.68

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |31725212351365685821171691849515008.00|
|VALIDATION    |-95940.61     |20.61         |
|TEST          |-98657.72     |19.89         |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.84         |15140312627405820.00|
|VALIDATION    |-171846.14    |141.07        |
|TEST          |-243876.13    |136.32        |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |250.68        |
|VALIDATION    |-43.51        |988.18        |
|TEST          |-42.85        |981.72        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.48         |3200930644450245345280.00|
|VALIDATION    |-3906229.33   |382.03        |
|TEST          |-4284854.64   |377.33        |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |13.86         |
|VALIDATION    |-17.89        |108.80        |
|TEST          |-19.78        |109.76        |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |4.48          |
|VALIDATION    |-243.51       |131.84        |
|TEST          |-310.78       |131.84        |

