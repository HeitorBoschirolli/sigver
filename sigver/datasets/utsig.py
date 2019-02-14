import os
from skimage.io import imread
from sigver.datasets.base import IterableDataset
from skimage import img_as_ubyte

from sigver.datasets.base import IterableDataset

class UTSIGDataset(IterableDataset):
    """ Helper class to load the UTSig dataset
    """

    def __init__(self, path):
        self.path = path
        self.users = list(range(1, 116))

    @property
    def genuine_per_user(self):
        return 0

    @property
    def skilled_per_user(self):
        return 27

    @property
    def simple_per_user(self):
        return 42

    @property
    def maxsize(self):
        return 1627, 2387

    def get_user_list(self):
        return self.users

    def iter_genuine(self, user):
        """ Iterate over genuine signatures for the given user"""

        all_files = sorted(os.listdir(self.path))
        user_genuine_files = filter(lambda x: x[4] == 'G', all_files)
        for f in user_genuine_files:
            full_path = os.path.join(self.path, f)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), f

    def iter_forgery(self, user):
        """ Iterate over skilled forgeries for the given user"""

        all_files = sorted(os.listdir(self.path))
        user_forgery_files = filter(lambda x: x[0:2] == 'cf', all_files)
        for f in user_forgery_files:
            full_path = os.path.join(self.path, f)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), f

    def get_signature(self, user, img_idx, forgery):
        """ Returns a particular signature (given by user id, img id and
            whether or not it is a forgery
        """

        if forgery:
            prefix = 'cf'
        else:
            prefix = 'c'
        filename = '{}-{:03d}-{:02d}.png'.format(prefix, user, img_idx)
        full_path = os.path.join(self.path, '{:03d}'.format(user), filename)
        return img_as_ubyte(imread(full_path, as_gray=True))

    def iter_simple_forgery(self, user):
        yield from ()  # No simple forgeries