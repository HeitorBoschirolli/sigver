.PHONY: background
results: bg_results_5_gen_utsig_170_242_signet.pickle \
		bg_results_5_gen_utsig_170_242_signet_f.pickle \
		bg_results_10_gen_utsig_170_242_signet.pickle \
		bg_results_10_gen_utsig_170_242_signet_f.pickle \
		bg_results_12_gen_utsig_170_242_signet.pickle \
		bg_results_12_gen_utsig_170_242_signet_f.pickle

.PHONY: bg_5_gen
bg_5_gen: bg_results_5_gen_utsig_170_242_signet.pickle \
	   bg_results_5_gen_utsig_170_242_signet_f.pickle

.PHONY: bg_10_gen
bg_10_gen: bg_results_10_gen_utsig_170_242_signet.pickle \
		bg_results_10_gen_utsig_170_242_signet_f.pickle

.PHONY: bg_12_gen
bg_12_gen: bg_results_12_gen_utsig_170_242_signet.pickle \
		bg_results_12_gen_utsig_170_242_signet_f.pickle

bg_results_5_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_5_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5

bg_results_5_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_5_gen_utsig_170_242_signet_f.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=5 \
	--gen-for-train=5

bg_results_10_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_10_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10

bg_results_10_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_10_gen_utsig_170_242_signet_f.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=10 \
	--gen-for-train=10

bg_results_12_gen_utsig_170_242_signet.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_12_gen_utsig_170_242_signet.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12

bg_results_12_gen_utsig_170_242_signet_f.pickle: bg_utsig_170_242.npz
	python -m sigver.wd.test -m signet \
	--model-path models/signet_f_lambda_0.95.pth \
	--data-path bg_utsig_170_242.npz \
	--save-path bg_results_12_gen_utsig_170_242_signet_f.pickle \
	--exp-users 1 116 \
	--forg-from_dev=0 \
	--forg-from_exp=12 \
	--gen-for-train=12

bg_utsig_170_242.npz: 
	python -m sigver.preprocessing.process_dataset \
	--dataset bg_utsig \
	--path data/bg_utsig \
	--save-path bg_utsig_170_242.npz

.PHONY: clean
clean:
	rm -f bg_utsig_170_242.npz \
	bg_results_5_gen_utsig_170_242_signet.pickle \
	bg_results_5_gen_utsig_170_242_signet_f.pickle \
	bg_results_10_gen_utsig_170_242_signet.pickle \
	bg_results_10_gen_utsig_170_242_signet_f.pickle \
	bg_results_12_gen_utsig_170_242_signet.pickle \
	bg_results_12_gen_utsig_170_242_signet_f.pickle