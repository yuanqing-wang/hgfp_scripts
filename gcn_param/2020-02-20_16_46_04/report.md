2020-02-20_16_46_04
===========================
# Model Summary
model=gcn_with_combine_readout
config=['256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu', '256', '0.1', 'relu']
hetero=False
data=QM9
batch_size=16
n_epochs=100
size=100
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
27.54

# Dataset Size
Training samples: 
Training: 64, Validation: 16, Test: 16
# Performance
atom_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.76          |0.02          |
|VALIDATION    |0.65          |0.03          |
|TEST          |0.40          |0.04          |


atom_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.97          |0.02          |
|VALIDATION    |0.94          |0.02          |
|TEST          |0.95          |0.02          |


bond_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.80          |81.48         |
|VALIDATION    |0.05          |153.34        |
|TEST          |0.64          |97.40         |


bond_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.66          |0.07          |
|VALIDATION    |0.35          |0.09          |
|TEST          |0.37          |0.10          |


angle_k

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.88          |52.20         |
|VALIDATION    |0.47          |121.37        |
|TEST          |0.10          |163.53        |


angle_eq

|              |R2            |RMSE          |
|------------- |------------- |------------- |
|TRAIN         |0.77          |14.10         |
|VALIDATION    |0.33          |23.04         |
|TEST          |0.17          |29.06         |

