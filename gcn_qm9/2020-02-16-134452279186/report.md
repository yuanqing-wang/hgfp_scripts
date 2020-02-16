2020-02-16-134452279186
===========================
# Model Summary
model=gcn
config=['256', 'tanh', '256', 'tanh', '256', 'tanh', '256', 'tanh', '256', 'tanh', '256', 'tanh', '1']
hetero=False
data=QM9
batch_size=32
n_epochs=200
size=10000
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_in_buffer=12
cache=True
n_batches_te=30
n_batches_vl=30
report=True

Net(
  (d0): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=10, out_features=256, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=256, bias=True)
    )
  )
  (d12): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=256, out_features=1, bias=True)
    )
  )
)
# Time Used 
3572.80

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.49          |186.29        |
|VALIDATION    |0.50          |186.10        |
|TEST          |0.49          |191.10        |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>