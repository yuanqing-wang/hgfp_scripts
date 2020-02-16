2020-02-16 02:08:56
===========================
# Model Summary
model=gcn
config=['128', 'tanh', '128', 'tanh', '128', 'tanh', '1']
hetero=False
data=QM9
batch_size=32
n_epochs=100
size=-1
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_in_buffer=12
cache=True
n_batches_te=418
n_batches_vl=418
report=True

Net(
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=10, out_features=128, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=1, bias=True)
    )
  )
)
# Time Used 
7015.71

# Dataset Size
Training samples: 
Training: 132865, Validation: 13377, Test: 13377
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.67          |139.42        |
|VALIDATION    |0.66          |139.78        |
|TEST          |0.67          |139.48        |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="rmse.jpg" width="600"></div>
<div align="center"><img src="r2.jpg" width="600"></div>