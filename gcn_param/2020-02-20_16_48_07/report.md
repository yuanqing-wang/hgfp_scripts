2020-02-20_16_48_07
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu']
hetero=False
data=QM9
batch_size=16
n_epochs=100
size=200
optimizer=Adam
learning_rate=0.001
loss_fn=mse_loss
n_batches_te=1
n_batches_vl=1
report=True

Net(
  (f_in): Sequential(
    (0): Linear(in_features=10, out_features=128, bias=True)
    (1): Tanh()
  )
  (f_in_e): Sequential(
    (0): Linear(in_features=13, out_features=128, bias=True)
    (1): Tanh()
  )
  (d0): GN(
    (d_phi_e): Linear(in_features=256, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=256, out_features=256, bias=True)
  )
  (readout): ParamReadout(
    (fr_atom): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_bond): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_torsion): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Linear(in_features=128, out_features=2, bias=True)
    )
    (fr_angle_0): Linear(in_features=768, out_features=256, bias=True)
    (fr_mol): Sequential(
      (0): Linear(in_features=256, out_features=128, bias=True)
      (1): Tanh()
      (2): Linear(in_features=128, out_features=1, bias=True)
    )
  )
  (d3): GN(
    (d_phi_e): Linear(in_features=512, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=512, out_features=256, bias=True)
  )
  (d6): GN(
    (d_phi_e): Linear(in_features=512, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=512, out_features=256, bias=True)
  )
  (d9): GN(
    (d_phi_e): Linear(in_features=512, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=512, out_features=256, bias=True)
  )
  (d12): GN(
    (d_phi_e): Linear(in_features=512, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=512, out_features=256, bias=True)
  )
  (d15): GN(
    (d_phi_e): Linear(in_features=512, out_features=256, bias=True)
    (d_phi_v): Linear(in_features=512, out_features=256, bias=True)
  )
)
# Time Used 
72.88

# Dataset Size
Training samples: 
Training: 160, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.86          |0.02          |
|VALIDATION    |0.57          |0.03          |
|TEST          |0.65          |0.03          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.98          |0.01          |
|VALIDATION    |0.97          |0.01          |
|TEST          |0.97          |0.02          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.81          |78.70         |
|VALIDATION    |0.67          |103.71        |
|TEST          |0.49          |120.77        |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.77          |0.05          |
|VALIDATION    |0.38          |0.08          |
|TEST          |0.34          |0.09          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.91          |35.95         |
|VALIDATION    |0.22          |176.89        |
|TEST          |0.38          |124.55        |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.79          |10.05         |
|VALIDATION    |0.34          |23.44         |
|TEST          |0.49          |21.16         |

