import numpy as np


class ScrapBooker:
    def __init__(self):
        pass

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position
        arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if (
            isinstance(array, np.ndarray) and
            isinstance(dim, tuple) and len(dim) == 2 and
            dim[0] >= 0 and dim[0] <= array.shape[0] and
            dim[1] >= 0 and dim[1] <= array.shape[1] and
            isinstance(position, tuple) and len(position) == 2 and
            position[0] >= 0 and position[0] <= array.shape[0] and
            position[1] >= 0 and position[1] <= array.shape[1]
        ):
            new_arr = np.array(
                array[position[0]:(dim[0]+1), position[1]:dim[1]]
            )
            return new_arr
        else:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column
                of the array (depending of axis value).
            axis: positive non null integer.
        Returns:
            new_arr: thined numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if (
            isinstance(array, np.ndarray) and
            isinstance(n, int) and n > 0 and
            isinstance(axis, int) and
            (
                (axis == 0 and n < array.shape[1]) or
                (axis == 1 and n < array.shape[0])
            )
        ):
            if axis == 0:
                return np.delete(
                    array,
                    list(range(n - 1, array.shape[1], n)),
                    1
                )
            else:
                return np.delete(
                    array,
                    list(range(n - 1, array.shape[0], n)),
                    0
                )
        else:
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if (
            isinstance(array, np.ndarray) and
            isinstance(n, int) and n > 0 and
            isinstance(axis, int) and
            (axis == 0 or axis == 1)
        ):
            if axis == 0:
                return np.concatenate([array] * n, 0)
            else:
                return np.tile(array, n)
        else:
            return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        if (
            isinstance(array, np.ndarray) and
            isinstance(dim, tuple) and len(dim) == 2 and
            dim[0] >= 0 and dim[1] >= 0
        ):
            return np.concatenate([np.tile(array, dim[0])] * dim[1], 0)
        else:
            return None
