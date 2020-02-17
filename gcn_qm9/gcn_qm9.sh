#BSUB -q cpuqueue
#BSUB -W 12:00


for unit in 32 64 128 256
do 
    for act in 'tanh' 'sigmoid' 'relu'
    do
        bsub -q gpuqueue -J gcn_qm9 -m "ld-gpu ls-gpu lt-gpu lg-gpu lu-gpu" -q gpuqueue -n 12 -gpu "num=1:j_exclusive=yes" -R "rusage[mem=4] span[hosts=1]" -W 8:00 -o %J.stdout -eo %J.stderr python ../../hgfp/hgfp/app/supervised_train.py --model gcn --batch_size 32 --size 10000 --n_batches_te 30 --n_batches_vl 30 --config $unit $act $unit $act $unit $act $unit $act $unit $act $unit $act 1 --learning_rate 1e-3 --n_epochs 200

    done
done



while true
do
    git add *
    git add */*
    git commit -m "[automated commit] updated data"
    git push https://yuanqing-wang:Ithinkthere4iam@github.com/choderalab/hgfp.git
    sleep 60
done
