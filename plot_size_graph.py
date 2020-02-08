""" plots a graph of the signatures size X correcte predictions """
import pickle

import matplotlib.pyplot as plt


RESULTS_FILE = ''


def main():
    """ runs the whole script """
    genuine_predictions, skilled_predictions = load_predictions()


def load_predictions():
    """ load the predictions """
    with open(RESULTS_FILE, 'rb') as results_file:
        results = pickle.load(results_file)

    # first cv only
    result = results[0]
    predictions = result['predictions']
    genuine_predictions = predictions['genuine_predictions']
    skilled_predictions = predictions['skilled_predictions']

    return genuine_predictions, skilled_predictions


if __name__ == '__main__':
    main()
