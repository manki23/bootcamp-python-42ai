import numpy as np


class NumPyCreator:
    def __init__(self):
        pass

    @staticmethod
    def from_list(lst):
        """
        Takes a list or nested list and returns its corresponding Numpy array
        """
        if (
            not isinstance(lst, list) or
            any(len(lst[0]) != len(elem) for elem in lst)
        ):
            return None
        else:
            return np.array(lst)

    @staticmethod
    def from_tuple(tpl):
        """
         takes a tuple or nested tuple and returns its corresponding Numpy
         array
        """
        if (
            not isinstance(tpl, tuple) or
            any(len(tpl[0]) != len(elem) for elem in tpl)
        ):
            return None
        else:
            return np.array(tpl)

    @staticmethod
    def from_iterable(itr):
        """
        takes an iterable and returns an array which contains all of
        its elements
        """
        if (
            not hasattr(itr, '__iter__')
        ):
            return None
        else:
            return np.fromiter(itr, dtype=None)

    @staticmethod
    def from_shape(shape, value=0.):
        """
         returns an array filled with the same value
         The first argument is a tuple which specifies the shape of the array
         The second argument specifies the value of all the elements.
         This value must be 0 by default
        """
        if (
            len(shape) == 2 and
            isinstance(shape[0], int) and shape[0] >= 0 and
            isinstance(shape[1], int) and shape[1] >= 0
        ):
            return np.full(shape, value)
        else:
            return None

    @staticmethod
    def random(shape):
        """
        returns an array filled with random values
        It takes as an argument a tuple which specifies the shape of the array
        """
        if (
            len(shape) == 2 and
            isinstance(shape[0], int) and shape[0] >= 0 and
            isinstance(shape[1], int) and shape[1] >= 0
        ):
            return np.random.rand(shape[0], shape[1])
        else:
            return None

    @staticmethod
    def identity(n):
        """
        returns an array representing the identity matrix of size n
        """
        if isinstance(n, int) and n >= 0:
            return np.identity(n)
        else:
            return None
