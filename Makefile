.PHONY: all
all: no_background background

####################
# Get the results for images without background
####################

.PHONY: no_background
no_background: results_5_gen_utsig_170_242_signet.pickle \
		 results_5_gen_utsig_170_242_signet_f.pickle \
		 results_10_gen_utsig_170_242_signet.pickle \
		 results_10_gen_utsig_170_242_signet_f.pickle \
		 results_12_gen_utsig_170_242_signet.pickle \
		 results_12_gen_utsig_170_242_signet_f.pickle

# preprocessing
.PHONY: 5_gen
5_gen: results_5_gen_utsig_170_242_signet.pickle \
	   results_5_gen_utsig_170_242_signet_f.pickle

.PHONY: 10_gen
10_gen: results_10_gen_utsig_170_242_signet.pickle \
		results_10_gen_utsig_170_242_signet_f.pickle

.PHONY: 12_gen
12_gen: results_12_gen_utsig_170_242_signet.pickle \
		results_12_gen_utsig_170_242_signet_f.pickle

# WD classifiers
results_5_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_5_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5 \
	--gen-for-test=22

results_5_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_5_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5 \
	--gen-for-test=22

results_10_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_10_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10 \
	--gen-for-test=17

results_10_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_10_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10 \
	--gen-for-test=17

results_12_gen_utsig_170_242_signet.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet --model-path models/signet.pth \
	--data-path utsig_170_242.npz \
	--save-path results_12_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12 \
	--gen-for-test=15

results_12_gen_utsig_170_242_signet_f.pickle: utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth --data-path utsig_170_242.npz \
	--save-path results_12_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12 \
	--gen-for-test=15

utsig_170_242.npz: 
	python -m sigver.preprocessing.process_dataset --dataset utsig \
	--path data/UTSig_Crop --save-path utsig_170_242.npz

###################
# Get the results for images with background
###################
#
.PHONY: background
background: bg_results_5_gen_utsig_170_242_signet.pickle \
		bg_results_5_gen_utsig_170_242_signet_f.pickle \
		bg_results_10_gen_utsig_170_242_signet.pickle \
		bg_results_10_gen_utsig_170_242_signet_f.pickle \
		bg_results_12_gen_utsig_170_242_signet.pickle \
		bg_results_12_gen_utsig_170_242_signet_f.pickle

# processing
.PHONY: bg_5_gen
bg_5_gen: bg_results_5_gen_utsig_170_242_signet.pickle \
	   bg_results_5_gen_utsig_170_242_signet_f.pickle

.PHONY: bg_10_gen
bg_10_gen: bg_results_10_gen_utsig_170_242_signet.pickle \
		bg_results_10_gen_utsig_170_242_signet_f.pickle

.PHONY: bg_12_gen
bg_12_gen: bg_results_12_gen_utsig_170_242_signet.pickle \
		bg_results_12_gen_utsig_170_242_signet_f.pickle

# WD classifiers
bg_results_5_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_5_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5

bg_results_5_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_5_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5

bg_results_10_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_10_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10

bg_results_10_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_10_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10

bg_results_12_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_12_gen_utsig_170_242_signet.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12

bg_results_12_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_12_gen_utsig_170_242_signet_f.pickle \
	--exp-users 0 115 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12

bg_utsig_170_242.npz: 
	python -m sigver.preprocessing.process_dataset \
	--dataset bg_utsig \
	--path data/bg_utsig \
	--save-path bg_utsig_170_242.npz

##################
# Clean
##################
.PHONY: clean
clean:
	rm -f utsig_170_242.npz \
	results_5_gen_utsig_170_242_signet.pickle \
	results_5_gen_utsig_170_242_signet_f.pickle \
	results_10_gen_utsig_170_242_signet.pickle \
	results_10_gen_utsig_170_242_signet_f.pickle \
	results_12_gen_utsig_170_242_signet.pickle \
	results_12_gen_utsig_170_242_signet_f.pickle \
	bg_utsig_170_242.npz \
	bg_results_5_gen_utsig_170_242_signet.pickle \
	bg_results_5_gen_utsig_170_242_signet_f.pickle \
	bg_results_10_gen_utsig_170_242_signet.pickle \
	bg_results_10_gen_utsig_170_242_signet_f.pickle \
	bg_results_12_gen_utsig_170_242_signet.pickle \
	bg_results_12_gen_utsig_170_242_signet_f.pickle
