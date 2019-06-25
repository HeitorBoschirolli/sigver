"""
Prints the EER for all users
"""
import pickle

FILE_NAME = 'tmp.pickle'


def main():
    """
    Runs the whole script
    """
    with open(FILE_NAME, 'rb') as results_file:
        results = pickle.load(results_file)

    print('=====EERs=====')
    for result in results:
        all_metrics = result['all_metrics']
        eer = all_metrics['EER']
        print(eer)

    print('\n=====user EERs=====')
    for result in results:
        all_metrics = result['all_metrics']
        eer = all_metrics['EER_userthresholds']
        print(eer)


if __name__ == '__main__':
    main()
