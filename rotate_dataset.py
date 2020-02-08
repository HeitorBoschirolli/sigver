import os
import random

import numpy as np
from skimage.io import imread, imsave
from skimage.transform import rotate
from skimage.filters import threshold_otsu
from skimage import img_as_float64


LOAD_DIR = 'data/mini_dataset'
SAVE_DIR = 'data/mini_augmented_dataset'
ROTATION = 20
AUGMENTING_FACTOR = 3


def main():
    """ main function """
    filenames = os.listdir(LOAD_DIR)
    filenames = filter(lambda x: x[4] == 'G', filenames)
    for filename in filenames:
        sig = load_signature(filename)
        augmented_signatures = [augment(sig) for _ in range(AUGMENTING_FACTOR)]
        save_augmented(filename, augmented_signatures)


def load_signature(filename):
    """ load a signature from the dataset """
    path = os.path.join(LOAD_DIR, filename)
    signature = imread(path, as_gray=True)
    signature = img_as_float64(signature)
    return signature


def augment(signature):
    """ augment a single signature """
    angle = random.randint(-ROTATION, ROTATION)
    rotated = rotate(signature, angle, resize=True, cval=1)
    no_bg = remove_background(rotated)
    no_border = remove_border(no_bg)
    return no_border


def remove_border(img):
    """ removes the white border of the image """
    neg_img = 1 - img

    pixels_on_col = np.sum(neg_img, axis=0)
    cols = np.nonzero(pixels_on_col > 0)[0]

    pixels_on_row = np.sum(neg_img, axis=1)
    rows = np.nonzero(pixels_on_row)[0]

    no_borders_img = img[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]
    import matplotlib.pyplot as plt
    from skimage.io import imshow
    import pdb; pdb.set_trace()
    return no_borders_img


def binarize(img, nl=3, method='otsu'):
    """ binarize the image """
    if method == 'posterization':
        post_img = np.round(img * nl) / nl
        return 1 - ((1 - post_img) > 0)
    if method == 'otsu':
        thresh = threshold_otsu(img)
        return img > thresh
    raise Exception('method not supported')


def remove_background(img, nl=3, method='posterization'):
    """ removes the noisy background """
    if len(img.shape) != 2:
        raise Exception('image must be in grayscale')

    bin_img = binarize(img, nl, method)
    no_bg_img = img
    no_bg_img[bin_img == 1] = 1
    return no_bg_img


def save_augmented(filename, signatures):
    """ save the augmented versions of a signature """
    assert len(signatures) * 45 < 1000
    assert len(signatures) == AUGMENTING_FACTOR

    sample_idx = int(filename[5:7])
    for idx, signature in enumerate(signatures):
        new_sample_idx = sample_idx * AUGMENTING_FACTOR + idx
        new_filename = f'{filename[:5]}{new_sample_idx:03d}{filename[-4:]}'
        path = os.path.join(SAVE_DIR, new_filename)
        imsave(path, signature)


if __name__ == '__main__':
    main()
