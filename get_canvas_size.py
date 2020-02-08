""" print the canvas size for a dataset in the stdout """
import os
from skimage.io import imread
from skimage import img_as_float64


DIRECTORY = 'data/UTSig_Crop'


def main():
    """ main function """
    max_rows, max_cols, _, _ = minmax(DIRECTORY)
    print(f'({max_rows}, {max_cols})')


def minmax(directory):
    """ get min and max n_rows and n_cols """
    img_names = [
        os.path.join(directory, name) for name in os.listdir(directory)
    ]

    max_rows = 0
    max_cols = 0
    min_rows = -1
    min_cols = -1
    for img_name in img_names:
        img = imread(img_name, as_gray=True)
        img = img_as_float64(img)

        rows, cols = img.shape

        if rows > max_rows:
            max_rows = rows
        if cols > max_cols:
            max_cols = cols
        if (rows < min_rows) or (min_rows == -1):
            min_rows = rows
        if (cols < min_cols) or (min_cols == -1):
            min_cols = cols

    return max_rows, max_cols, min_rows, min_cols


if __name__ == '__main__':
    main()
