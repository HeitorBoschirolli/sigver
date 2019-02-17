import numpy as np
from skimage.io import imread
from skimage import img_as_ubyte
from utsig import UTSIGDataset


utsig_dataset = UTSIGDataset('/home/hboschirolli/academico/projects/ic/sigver/data/UTSig_Crop/')


def genuine_per_user_test():
    actual = utsig_dataset.genuine_per_user
    expected = 27

    assert(actual == expected)


def skilled_per_user_test():
    actual = utsig_dataset.skilled_per_user
    expected = 42

    assert(actual == expected)


def simple_per_user_test():
    actual = utsig_dataset.simple_per_user
    expected = 0

    assert(actual == expected)


def maxsize_test():
    actual = utsig_dataset.maxsize
    expected = (1627, 2387)


def get_user_list():
    actual = utsig_dataset.get_user_list()
    expected = list(range(1, 116))
    assert(actual == expected)


def iter_genuine_test():
    actual_img, actual_name = next(utsig_dataset.iter_genuine(1))
    expected_img = img_as_ubyte(
        imread('/home/hboschirolli/academico/projects/ic/sigver/data/UTSig_Crop/C001G01.PNG', as_gray=True)
    )
    expected_name = 'C001G01.PNG'
    
    assert(actual_img == expected_img).all()
    assert(actual_name == expected_name)


def iter_forgery_test():
    actual_img, actual_name = next(utsig_dataset.iter_forgery(1))
    expected_img = img_as_ubyte(
        imread('/home/hboschirolli/academico/projects/ic/sigver/data/UTSig_Crop/C001F01.PNG', as_gray=True)
    )
    expected_name = 'C001F01.PNG'
    
    assert(actual_img == expected_img).all()
    assert(actual_name == expected_name)


if __name__ == "__main__":
    genuine_per_user_test()
    skilled_per_user_test()
    simple_per_user_test()
    maxsize_test()
    get_user_list()
    iter_genuine_test()
    iter_forgery_test()
