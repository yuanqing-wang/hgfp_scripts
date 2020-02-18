2020-02-17_20_34_11
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', 'tanh', '32']
hetero=False
data=QM9
batch_size=16
n_epochs=1
size=200
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=10, out_features=32, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=32, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=32, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=32, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=32, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=32, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
)
# Time Used 
0.23

# Dataset Size
Training samples: 
Training: 160, Validation: 16, Test: 16
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-2.25         |0.08          |
|VALIDATION    |-3.06         |0.09          |
|TEST          |-2.10         |0.09          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-400.86       |1.74          |
|VALIDATION    |-477.90       |1.74          |
|TEST          |-340.52       |1.72          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-17.76        |779.47        |
|VALIDATION    |-23.38        |720.43        |
|TEST          |-17.51        |836.60        |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-141.92       |1.32          |
|VALIDATION    |-145.42       |1.35          |
|TEST          |-119.91       |1.28          |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-1.45         |212.63        |
|VALIDATION    |-1.30         |215.16        |
|TEST          |-38.57        |132.67        |


|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |-25.63        |118.57        |
|VALIDATION    |-19.35        |116.53        |
|TEST          |-32.58        |126.03        |

