""" small version of the augmented utsig dataset (for testing) """
import os

from skimage import img_as_ubyte
from skimage.io import imread

from sigver.datasets.base import IterableDataset


class AugmentedMiniUTSIGDataset(IterableDataset):
    """ Helper class to load the UTSig dataset
    """

    def __init__(self, path):
        self.path = path
        self.users = list(range(1, 3))

    @property
    def genuine_per_user(self):
        return 27 * 3

    @property
    def skilled_per_user(self):
        return 0

    @property
    def simple_per_user(self):
        return 0

    @property
    def maxsize(self):
        return 4314, 4353

    def get_user_list(self):
        return self.users

    def iter_genuine(self, user):
        """ Iterate over genuine signatures for the given user"""

        all_files = sorted(os.listdir(self.path))
        user_files = filter(lambda x: int(x[1:4]) == int(user), all_files)
        user_genuine_files = filter(lambda x: x[4] == 'G', user_files)
        for f in user_genuine_files:
            full_path = os.path.join(self.path, f)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), f

    def iter_forgery(self, user):
        yield from ()  # No skilled forgeries

    def iter_simple_forgery(self, user):
        yield from ()  # No simple forgeries
