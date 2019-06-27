""" augment utsig dataset """
import os
import random
import math

import numpy as np
from skimage.io import imread, imsave
from skimage.util import pad


LOAD_DIR = 'data/UTSig_Crop'
SAVE_DIR = 'data/augmented_utsig'
TRANSLATION = 0.2
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
    if signature.dtype == 'float64':
        signature *= 255
        signature = signature.astype('uint8')
    return signature


def augment(signature):
    """ augment a single signature """
    max_row_padding = math.ceil(TRANSLATION * signature.shape[0])
    max_col_padding = math.ceil(TRANSLATION * signature.shape[1])

    top = random.randint(0, max_row_padding)
    bot = max_row_padding - top

    left = random.randint(0, max_col_padding)
    right = max_col_padding - left

    return pad(signature, ((top, bot), (left, right)),
               'constant', constant_values=255)


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
