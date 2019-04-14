.PHONY: all
results: results_5_gen_utsig_170_242_signet.pickle \
		 results_5_gen_utsig_170_242_signet_f.pickle \
		 results_10_gen_utsig_170_242_signet.pickle \
		 results_10_gen_utsig_170_242_signet_f.pickle \
		 results_12_gen_utsig_170_242_signet.pickle \
		 results_12_gen_utsig_170_242_signet_f.pickle

.PHONY: 5_gen
5_gen: results_5_gen_utsig_170_242_signet.pickle \
	   results_5_gen_utsig_170_242_signet_f.pickle

.PHONY: 10_gen
10_gen: results_10_gen_utsig_170_242_signet.pickle \
		results_10_gen_utsig_170_242_signet_f.pickle

.PHONY: 12_gen
12_gen: results_12_gen_utsig_170_242_signet.pickle \
		results_12_gen_utsig_170_242_signet_f.pickle

results_5_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_5_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 --forg-from_dev=0 --forg-from_exp=5 --gen-for-train=5

results_5_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_5_gen_utsig_170_242_signet_f.pickle --exp-users 1 116 \
	--forg-from_dev=0 --forg-from_exp=5 --gen-for-train=5

results_10_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_10_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 --forg-from_dev=0 --forg-from_exp=10 --gen-for-train=10

results_10_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_10_gen_utsig_170_242_signet_f.pickle --exp-users 1 116 \
	--forg-from_dev=0 --forg-from_exp=10 --gen-for-train=10

results_12_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_12_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 --forg-from_dev=0 --forg-from_exp=12 --gen-for-train=12


results_12_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_12_gen_utsig_170_242_signet_f.pickle --exp-users 1 116 \
	--forg-from_dev=0 --forg-from_exp=12 --gen-for-train=12

utsig_170_242.npz: 
	python -m sigver.preprocessing.process_dataset --dataset utsig \
	--path data/UTSig_Crop --save-path utsig_170_242.npz

.PHONY: clean
clean:
	rm -f utsig_170_242.npz \
	results_5_gen_utsig_170_242_signet.pickle \
	results_5_gen_utsig_170_242_signet_f.pickle \
	results_10_gen_utsig_170_242_signet.pickle \
	results_10_gen_utsig_170_242_signet_f.pickle \
	results_12_gen_utsig_170_242_signet.pickle \
	results_12_gen_utsig_170_242_signet_f.pickle