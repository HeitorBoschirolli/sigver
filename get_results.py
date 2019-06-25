"""
Separetes the errors made by the classifiers.
"""
import pickle
from statistics import stdev, mean


# using signet and simple background
SIMPLE_SIGNET_5_FILE = 'results_5_gen_utsig_170_242_signet.pickle'
SIMPLE_SIGNET_10_FILE = 'results_10_gen_utsig_170_242_signet.pickle'
SIMPLE_SIGNET_12_FILE = 'results_12_gen_utsig_170_242_signet.pickle'
# using signet_f and simple background
SIMPLE_SIGNET_F_5_FILE = 'results_5_gen_utsig_170_242_signet_f.pickle'
SIMPLE_SIGNET_F_10_FILE = 'results_10_gen_utsig_170_242_signet_f.pickle'
SIMPLE_SIGNET_F_12_FILE = 'results_12_gen_utsig_170_242_signet_f.pickle'
# using signet and complex background
# COMPLEX_SIGNET_5_FILE = 'bg_results_5_gen_utsig_170_242_signet.pickle'
# COMPLEX_SIGNET_10_FILE = 'bg_results_10_gen_utsig_170_242_signet.pickle'
# COMPLEX_SIGNET_12_FILE = 'bg_results_12_gen_utsig_170_242_signet.pickle'
# using signet_f and complex background
# COMPLEX_SIGNET_F_5_FILE = 'bg_results_5_gen_utsig_170_242_signet_f.pickle'
# COMPLEX_SIGNET_F_10_FILE = 'bg_results_10_gen_utsig_170_242_signet_f.pickle'
# COMPLEX_SIGNET_F_12_FILE = 'bg_results_12_gen_utsig_170_242_signet_f.pickle'


def load_results(file_name):
    """
    Load the results from a pickle file
    """
    with open(file_name, 'rb') as results_file:
        results = pickle.load(results_file)
    return results

def list_eer(results):
    return [cv['all_metrics']['EER'] for cv in results]

def calculate_stats(file_name):
    results = load_results(file_name)
    eers = list_eer(results)
    eers_mean = mean(eers)
    eers_stdev = stdev(eers)
    return eers_mean, eers_stdev


if __name__ == '__main__':
    do_simple_signet_5 = True
    do_simple_signet_10 = True
    do_simple_signet_12 = True
    do_simple_signet_f_5 = True
    do_simple_signet_f_10 = True
    do_simple_signet_f_12 = True
    # do_complex_signet_5 = True
    # do_complex_signet_10 = True
    # do_complex_signet_12 = True
    # do_complex_signet_f_5 = True
    # do_complex_signet_f_10 = True
    # do_complex_signet_f_12 = True

    dictionary = {}
    if do_simple_signet_5:
        dictionary['simple_signet_5'] = calculate_stats(SIMPLE_SIGNET_5_FILE)
    if do_simple_signet_10:
        dictionary['simple_signet_10'] = calculate_stats(SIMPLE_SIGNET_10_FILE)
    if do_simple_signet_12:
        dictionary['simple_signet_12'] = calculate_stats(SIMPLE_SIGNET_12_FILE)
    if do_simple_signet_f_5:
        dictionary['simple_signet_f_5'] = calculate_stats(SIMPLE_SIGNET_F_5_FILE)
    if do_simple_signet_f_10:
        dictionary['simple_signet_f_10'] = calculate_stats(SIMPLE_SIGNET_F_10_FILE)
    if do_simple_signet_f_12:
        dictionary['simple_signet_f_12'] = calculate_stats(SIMPLE_SIGNET_F_12_FILE)
    # if do_complex_signet_5:
        # dictionary['complex_signet_5'] = calculate_stats(COMPLEX_SIGNET_5_FILE)
    # if do_complex_signet_10:
        # dictionary['complex_signet_10'] = calculate_stats(COMPLEX_SIGNET_10_FILE)
    # if do_complex_signet_12:
        # dictionary['complex_signet_12'] = calculate_stats(COMPLEX_SIGNET_12_FILE)
    # if do_complex_signet_f_5:
        # dictionary['complex_signet_f_5'] = calculate_stats(COMPLEX_SIGNET_F_5_FILE)
    # if do_complex_signet_f_10:
        # dictionary['complex_signet_f_10'] = calculate_stats(COMPLEX_SIGNET_F_10_FILE)
    # if do_complex_signet_f_12:
        # dictionary['complex_signet_f_12'] = calculate_stats(COMPLEX_SIGNET_F_12_FILE)

    print('model \t\t\t EER mean \t\t\t EER stdev')
    for key in dictionary:
        print(f'{key} \t\t\t {dictionary[key][0]} \t\t\t {dictionary[key][1]}')
