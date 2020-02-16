#BSUB -q gpuqueue
#BSUB -J gcn_qm9
#BSUB -m "ld-gpu ls-gpu lt-gpu lp-gpu lg-gpu lv-gpu lu-gpu"
#BSUB -q gpuqueue -n 12 -gpu "num=1:j_exclusive=yes"
#BSUB -R "rusage[mem=4] span[hosts=1]"
#BSUB -W 8:00
#BSUB -o %J.stdout
#BSUB -eo %J.stderr

python ../../hgfp/hgfp/app/supervised_train.py --model gcn --batch_size 32 --n_batches_te 418 --n_batches_vl 418 --config 128 'tanh' 128 'tanh' 128 'tanh' 1 --learning_rate 1e-3 --n_epochs 100

git add *
git commit -m "[automated commit] updated data"
git push https://yuanqing-wang:Ithinkthere4iam@github.com/choderalab/hgfp.git
