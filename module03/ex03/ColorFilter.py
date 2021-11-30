import numpy as np
import copy


class ColorFilter:
    def __init__(self):
        pass

    @staticmethod
    def invert(array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            return 1 - array[..., :3]
        else:
            return None

    @staticmethod
    def to_blue(array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            return np.dstack((np.zeros(array.shape)[..., 2:], array[..., 2:]))
        else:
            return None

    @staticmethod
    def to_green(array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            array_deepcopy = copy.deepcopy(array)
            array_deepcopy[..., :1] = array_deepcopy[..., :1] * 0
            array_deepcopy[..., 2:3] = array_deepcopy[..., 2:3] * 0
            return array_deepcopy
        else:
            return None

    @staticmethod
    def to_red(array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            blue = ColorFilter.to_blue(array)
            green = ColorFilter.to_green(array)
            return array[..., :3] - (blue + green)[..., :3]
        else:
            return None

    @staticmethod
    def to_celluloid(array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            darray = copy.deepcopy(array)
            for color in range(0, 3):
                color_min = darray[:, :, color].min()
                color_max = darray[:, :, color].max()
                c_inter = np.linspace(color_min, color_max, 5)

                for i in range(0, 5):
                    inter = darray[:, :, color] <= c_inter[i]
                    if i > 0:
                        inter = inter & (darray[:, :, color] > c_inter[i - 1])
                    avg = np.average(darray[:, :, color][inter])
                    darray[:, :, color][inter] = avg
            return darray
        else:
            return None

    @staticmethod
    def to_grayscale(array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        pass
