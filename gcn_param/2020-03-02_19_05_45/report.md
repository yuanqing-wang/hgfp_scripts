2020-03-02_19_05_45
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
2.62

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-0.01         |30326614226126332944463210773217280.00|
|VALIDATION    |-0.06         |0.07          |
|TEST          |-0.04         |0.07          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-5.57         |12706636718521332.00|
|VALIDATION    |-0.26         |0.35          |
|TEST          |-0.40         |0.31          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |618.83        |
|VALIDATION    |-1.57         |243.93        |
|TEST          |-1.42         |244.18        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.47         |3219263116456273379328.00|
|VALIDATION    |-1.94         |0.32          |
|TEST          |-2.01         |0.31          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |121.47        |
|VALIDATION    |-0.01         |46.49         |
|TEST          |0.04          |24.32         |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.00          |124.56        |
|VALIDATION    |-2.47         |13.66         |
|TEST          |-2.70         |13.87         |

