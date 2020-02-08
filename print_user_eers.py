""" print eer mean and stdev for each author """
import pickle
from statistics import mean, stdev

import numpy as np
import sklearn.metrics as sk_metrics

from print_accs import print_vars
from sigver.wd.metrics import calculate_EER_user_thresholds

FILE_NAME = 'tmp.pickle'


def main():
    """ main function """
    genuine_predictions, skilled_predictions = load_predictions()
    n_users = len(genuine_predictions[0])
    users = list(range(0, n_users))

    genuine_predictions = np.array(genuine_predictions)
    skilled_predictions = np.array(skilled_predictions)

    means = list()
    stdevs = list()

    for user in users:
        eers = list()
        # thresholds = list()

        user_genuine_preds = genuine_predictions[:, user]
        user_skilled_preds = skilled_predictions[:, user]

        for cv_ugp, cv_usp in zip(user_genuine_preds, user_skilled_preds):
            # eer, threshold = compute_eer(cv_ugp, cv_usp)
            eer = calculate_EER_user_thresholds([cv_ugp], [cv_usp])
            eers.append(eer)
            # thresholds.append(threshold)

        means.append(mean(eers))
        stdevs.append(stdev(eers))

    metrics = sorted(zip(means, stdevs, users), key=lambda x: x[0])
    means_mean = list()

    for split_mean, split_stdev, user in metrics:
        means_mean.append(split_mean)
        user_metrics = {'eer_mean': split_mean, 'eer_stdev': split_stdev}
        # user + 1 because the user array id starts at 0 and the user dataset
        # id starts at 1
        print_vars(title=f'user {user + 1} metrics', **user_metrics)

    print_vars(title='dataset metrics',
               **calculate_dataset_eer(genuine_predictions,
                                       skilled_predictions))
    print_vars(title='mean\'s mean', means_mean=sum(means_mean)/len(means_mean))


def calculate_dataset_eer(genuine_predictions, skilled_predictions):
    """ computes the dataset eer with user threshold """
    assert len(genuine_predictions) == len(skilled_predictions)
    n_splits = len(genuine_predictions)
    splits = range(n_splits)

    eers = list()
    for split in splits:
        split_gen_pred = genuine_predictions[split]
        split_ski_pred = skilled_predictions[split]

        eer = calculate_EER_user_thresholds(split_gen_pred, split_ski_pred)
        eers.append(eer)

    eer_mean = mean(eers)
    eer_stdev = stdev(eers)
    metrics = {'eer_mean': eer_mean, 'eer_stdev': eer_stdev}

    return metrics


def compute_all_users_eer(genuine_preds, skilled_preds):
    """ computes eer mean and stdev for all dataset """
    all_genuine_preds = np.concatenate(list(genuine_preds))
    all_skilled_preds = np.concatenate(list(skilled_preds))

    eers = list()
    thresholds = list()
    for cv_gp, cv_sp in zip(list(all_genuine_preds), list(all_skilled_preds)):
        eer, threshold = compute_eer(cv_gp, cv_sp)
        eers.append(eer)
        thresholds.append(threshold)

    stats = {'eer_mean': mean(eers), 'eer_stdev': stdev(eers)}
    return stats


def compute_eer(genuine_preds, skilled_preds):
    """ compute the eer """
    all_preds = np.concatenate([genuine_preds, skilled_preds])
    all_ys = np.concatenate([np.ones_like(genuine_preds),
                             np.ones_like(skilled_preds) * -1])
    fpr, tpr, thresholds = sk_metrics.roc_curve(all_ys, all_preds)

    # Select the threshold closest to (FPR = 1 - TPR)
    eer_threshold = thresholds[sorted(enumerate(abs(fpr - (1 - tpr))),
                                      key=lambda x: x[1])[0][0]]
    genuine_errors = 1 - np.mean(genuine_preds >= eer_threshold).item()
    skilled_errors = 1 - np.mean(skilled_preds < eer_threshold).item()
    eer = (genuine_errors + skilled_errors) / 2.0
    return eer, eer_threshold


def load_predictions():
    """ load the predictions from the pickle file """
    with open(FILE_NAME, 'rb') as results_file:
        results = pickle.load(results_file)

    preds = [result['predictions'] for result in results]
    genuine_predictions = [cv_preds['genuinePreds'] for cv_preds in preds]
    skilled_predictions = [cv_preds['skilledPreds'] for cv_preds in preds]

    return genuine_predictions, skilled_predictions


if __name__ == '__main__':
    main()
