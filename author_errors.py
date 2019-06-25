"""
Get the errors for each author over all the cross-validation splits
"""
import pickle
import numpy as np


N_AUTHORS = 115

def main():
    """
    Function to run the whole script
    """
    with open('result_5_gen_utsig_170_252_signet.pickle', 'rb') as results_file:
        results = pickle.load(results_file)
    return author_errors(results)


def author_errors(results):
    """
    Get the errors for each author in one cross-validation split
    """
    false_positives = np.zeros(10,)
    false_negatives = np.zeros(10,)
    for cv_result in results:
        author_false_positives, author_false_negatives = author_error(cv_result)
        false_positives += author_false_positives
        false_negatives += author_false_negatives


def author_error(results):
    """
    Get the errors for one author in one cross-validation split
    Return:
    false_positives: numpy.ndarray
    false_negatives: numpy.ndarray
    """
    predictions = results['predictions']
    genuine_predictions = predictions['genuinePreds']
    random_predictions = predictions['randomPreds']
    skilled_predictions = predictions['skilledPreds']

    # the number of authors must be the same in every set
    assert len(genuine_predictions) == len(random_predictions)
    assert len(random_predictions) == len(skilled_predictions)
    assert len(skilled_predictions) == N_AUTHORS

    return np.zeros(10,), np.zeros(10,)
