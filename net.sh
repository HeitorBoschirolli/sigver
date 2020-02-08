python -m sigver.wd.test -m signet --model-path models/signet.pth --data-path \
    tmp.npz --save-path tmp.pickle --exp-users 0 2 \
    --forg-from_dev=0 --forg-from_exp=12 --gen-for-train=12 --folds=10 \
    --gen-for-test=15 --augmented-path augmented_tmp.npz

