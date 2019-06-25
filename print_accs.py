"""
Prints the accuracy for each user in the first cv split
"""
import pickle
from statistics import mean, stdev


FILE_NAME = 'results_12_gen_utsig_170_242_signet_f.pickle'

def main():
    """
    Runs the whole script
    """
    with open(FILE_NAME, 'rb') as results_file:
        results = pickle.load(results_file)

    users = get_users(results)

    for user in users:
        get_user_metrics(results, user)

def get_user_metrics(results, user, verbose=1):
    false_positives = list()
    false_negatives = list()
    accuracies = list()

    for result in results:
        predictions = result['predictions']
        genuine_predictions = predictions['genuinePreds']
        skilled_predictions = predictions['skilledPreds']

        metrics = get_user_cv_metrics(genuine_predictions,
                                      skilled_predictions, user)

        false_positives.append(metrics['false_positives'])
        false_negatives.append(metrics['false_negatives'])
        accuracies.append(metrics['accuracy'])

    acc_mean = mean(accuracies)
    acc_stdev = stdev(accuracies) if len(accuracies) > 1 else None
    # fp_mean = mean(false_positives)
    # fp_stdev = stdev(false_positives)
    # fn_mean = mean(false_negatives)
    # fn_stdev = mean(false_negatives)

    if verbose == 1:
        print_vars(f'user {user} accuracies', acc_mean=acc_mean,
                   acc_stdev=acc_stdev)


def get_user_cv_metrics(genuine_predictions, skilled_predictions, user):
    metrics = dict()

    true_positives, false_negatives = pos_and_neg(genuine_predictions[user])
    false_positives, true_negatives = pos_and_neg(skilled_predictions[user])
    positives = true_positives + false_negatives
    negatives = true_negatives + false_positives
    accuracy = (true_positives + true_negatives) / (positives + negatives)

    metrics['true_positives'] = true_positives
    metrics['true_negatives'] = true_negatives
    metrics['false_positives'] = false_positives
    metrics['false_negatives'] = false_negatives
    metrics['accuracy'] = accuracy

    return metrics

def get_users(results):
    result = results[0]
    predictions = result['predictions']
    n_users = len(predictions['genuinePreds'])
    return list(range(0, n_users))

def cv_stats(result):
    predictions = result['predictions']
    genuine_predictions = predictions['genuinePreds']
    skilled_predictions = predictions['skilledPreds']

    metrics = stats(genuine_predictions, skilled_predictions, True)

    return find_accuracy(true_positives=metrics['true_positives'],
                         true_negatives=metrics['true_negatives'],
                         false_positives=metrics['false_positives'],
                         false_negatives=metrics['false_negatives'])

def stats(genuine_predictions, skilled_predictions, verbose=1):
    """
    Calculates false positives, false negatives, true positives and
    true negatives for all the users
    """
    assert len(genuine_predictions) == len(skilled_predictions)

    metrics = {'false_positives': 0,
               'false_negatives': 0,
               'true_positives': 0,
               'true_negatives': 0}
    accuracies = list()

    for i, _ in enumerate(genuine_predictions):
        true_positives, false_negatives = pos_and_neg(genuine_predictions[i])
        false_positives, true_negatives = pos_and_neg(skilled_predictions[i])

        accuracy = find_accuracy(true_positives=true_positives,
                                 true_negatives=true_negatives,
                                 false_positives=false_positives,
                                 false_negatives=false_negatives)
        accuracies.append(accuracy)

        metrics['false_positives'] += false_positives
        metrics['false_negatives'] += false_negatives
        metrics['true_positives'] += true_positives
        metrics['true_negatives'] += true_negatives

        if verbose == 1:
            print_vars(title=f'metrics for author{i}',
                       accuraccy=accuracy,
                       false_positives=false_positives,
                       false_negatives=false_negatives)

    if verbose == 1:
        accuracies, idx = sort_n(accuracies, range(len(accuracies)))
        best_accs_dict = dictionarize(idx[-5:], accuracies[-5:], 'Author id ')
        worst_accs_dict = dictionarize(idx[:5], accuracies[:5], 'Author id ')
        print_vars(title='best accuracies', **best_accs_dict)
        print_vars(title='worst accuracies', **worst_accs_dict)

    return metrics
def pos_and_neg(predictions):
    """
    Calculate the number of positive and negative predictions
    """
    negatives = 0
    positives = 0
    for prediction in predictions:
        if prediction < 0:
            negatives += 1
        else:
            positives += 1
    return positives, negatives

def find_accuracy(true_positives, true_negatives, false_positives, false_negatives):
    """
    Calculates the accuracy given the true positives, true negatives, false
    postitives and false negatives
    """
    trues = true_positives + true_negatives
    falses = false_positives + false_negatives
    return trues / (trues + falses)

def print_vars(title=None, **kargs):
    """
    Prints the parameters
    """
    if title is not None:
        print(f'========== {title} ==========')
    else:
        print('========== ==========')
    for key in kargs:
        print(f'{key}: {kargs[key]}')

def sort_n(keys, *lists):
    """
    Sorts n lists usings the 'keys' list
    """
    tups = sorted(zip(keys, *lists))
    return (list(t) for t in zip(*tups))

def dictionarize(keys, values, keys_app=''):
    """
    Returns a dictionary made of the lists passed as parameters. If the keys
    are strings it is possible to append a constant to the start of every key
    with the keys_app parameter.
    """
    dictionary = dict()
    for key, value in zip(keys, values):
        dictionary[f'{keys_app}{str(key)}'] = value

    return dictionary


if __name__ == '__main__':
    main()
