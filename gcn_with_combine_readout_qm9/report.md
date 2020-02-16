2020-02-16-135143672519
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', 'sigmoid', '32', 'sigmoid', '32', 'sigmoid', '32', 'sigmoid', '32', 'sigmoid', '32', 'sigmoid']
hetero=True
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
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
)
# Time Used 
4465.59

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |26.50         |
|VALIDATION    |0.99          |26.40         |
|TEST          |0.99          |27.01         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135205454601
===========================
# Model Summary
model=gcn_with_combine_readout
config=['128', 'tanh', '128', 'tanh', '128', 'tanh', '128', 'tanh', '128', 'tanh', '128', 'tanh']
hetero=True
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
      (linear): Linear(in_features=10, out_features=128, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=128, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=128, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=128, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=128, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=128, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
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
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=128, out_features=128, bias=True)
    )
  )
)
# Time Used 
4822.11

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.94          |64.97         |
|VALIDATION    |0.94          |65.97         |
|TEST          |0.94          |62.41         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135208242681
===========================
2020-02-16-135210467232
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'sigmoid', '256', 'sigmoid', '256', 'sigmoid', '256', 'sigmoid', '256', 'sigmoid', '256', 'sigmoid']
hetero=True
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
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
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
)
# Time Used 
7221.30

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |19.68         |
|VALIDATION    |0.99          |19.28         |
|TEST          |0.99          |19.23         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135211533356
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', 'relu', '32', 'relu', '32', 'relu', '32', 'relu', '32', 'relu', '32', 'relu']
hetero=True
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
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
)
# Time Used 
4574.95

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |1.00          |17.89         |
|VALIDATION    |1.00          |18.42         |
|TEST          |1.00          |17.46         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135211596672
===========================
# Model Summary
model=gcn_with_combine_readout
config=['64', 'tanh', '64', 'tanh', '64', 'tanh', '64', 'tanh', '64', 'tanh', '64', 'tanh']
hetero=True
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
      (linear): Linear(in_features=10, out_features=64, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
)
# Time Used 
4673.07

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |24.01         |
|VALIDATION    |0.99          |23.99         |
|TEST          |0.99          |24.98         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135213519220
===========================
2020-02-16-135217056866
===========================
2020-02-16-135224822901
===========================
2020-02-16-135231815477
===========================
# Model Summary
model=gcn_with_combine_readout
config=['32', 'tanh', '32', 'tanh', '32', 'tanh', '32', 'tanh', '32', 'tanh', '32', 'tanh']
hetero=True
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
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=32, out_features=32, bias=True)
    )
  )
)
# Time Used 
4603.28

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.99          |21.16         |
|VALIDATION    |0.99          |21.11         |
|TEST          |0.99          |21.44         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135236016114
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu', '256', 'relu']
hetero=True
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
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
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
)
# Time Used 
8704.76

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |1.00          |15.35         |
|VALIDATION    |1.00          |15.09         |
|TEST          |1.00          |14.54         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>2020-02-16-135258280162
===========================
# Model Summary
model=gcn_with_combine_readout
config=['64', 'relu', '64', 'relu', '64', 'relu', '64', 'relu', '64', 'relu', '64', 'relu']
hetero=True
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
      (linear): Linear(in_features=10, out_features=64, bias=True)
    )
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=2, bias=True)
    )
    (fr_mol): Sequential(
      (0): Linear(in_features=64, out_features=32, bias=True)
      (1): Tanh()
      (2): Linear(in_features=32, out_features=1, bias=True)
    )
  )
  (d2): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d4): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d6): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d8): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
  (d10): GCN(
    (apply_mod): NodeFullyConnect(
      (linear): Linear(in_features=64, out_features=64, bias=True)
    )
  )
)
# Time Used 
5049.57

# Dataset Size
Training samples: 
Training: 9985, Validation: 961, Test: 961
# Performance
|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |1.00          |16.59         |
|VALIDATION    |1.00          |17.05         |
|TEST          |1.00          |16.64         |

<div align="center"><img src="loss.jpg" width="600"></div>
<div align="center"><img src="RMSE.jpg" width="600"></div>
<div align="center"><img src="R2.jpg" width="600"></div>