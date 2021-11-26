import sys
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageProcessor:

    def __init__(self):
        pass

    @staticmethod
    def load(path: str):
        """
        Opens the .png file specified by the path argument and returns an
        array with the RGB values of the image pixels It must display a message
        specifying the dimensions of the image (e.g. 340 x 500)
        """
        try:
            pic = mpimg.imread(path)
            print(f"Loading image of dimensions {pic.shape[0]} x ",
                  f"{pic.shape[1]}")
            return np.array(pic)
        except Exception as e:
            if hasattr(e, 'strerror'):
                stderror = e.strerror
            elif hasattr(e, 'msg'):
                stderror = e.msg
            else:
                stderror = ''
            print(f"Exception: {e.__class__.__name__} -- ",
                  f"strerror: {stderror}", file=sys.stderr)

    @staticmethod
    def display(array):
        """
        Takes a numpy array as an argument and displays the corresponding
        RGB image
        """
        if (isinstance(array, np.ndarray)):
            plt.axis('off')
            plt.imshow(array)
            plt.show()
        pass
