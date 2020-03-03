2020-03-02_19_04_15
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
2.60

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |32312038351557630073166745699352576.00|
|VALIDATION    |0.27          |0.05          |
|TEST          |0.29          |0.06          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.51         |15527506906104420.00|
|VALIDATION    |-0.35         |0.33          |
|TEST          |-0.33         |0.34          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |989.34        |
|VALIDATION    |-1.30         |227.48        |
|TEST          |-1.61         |245.20        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.42         |3150283117244208119808.00|
|VALIDATION    |-0.34         |0.20          |
|TEST          |-0.39         |0.23          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |112.14        |
|VALIDATION    |-0.42         |29.39         |
|TEST          |-0.34         |29.13         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |135.64        |
|VALIDATION    |-0.17         |7.31          |
|TEST          |-0.19         |7.65          |

