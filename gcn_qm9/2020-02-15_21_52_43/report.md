2020-02-15 21:52:43
===========================
# Model Summary
model=gcn
config=['32', 'tanh', '32', 'tanh', '1']
hetero=False
data=QM9
batch_size=32
n_epochs=30
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
      (linear): Linear(in_features=10, out_features=32, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=1, bias=True)
    )
  )
)

# Time Used 
1017.32

# Performance