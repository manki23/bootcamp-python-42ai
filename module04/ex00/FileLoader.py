import sys
import numpy as np
import pandas as pd


class FileLoader:
    def __init__(self):
        pass

    @staticmethod
    def load(path):
        """
        - Takes as an argument the file path of the dataset to load,
        - Displays a message specifying the dimensions of the dataset
            (e.g. 340 x 500)
        - And returns the dataset loaded as a pandas.DataFrame
        """
        try:
            arr = pd.read_csv(path)
            print(f"Loading dataset of dimensions {arr.shape[0]} x ",
                  f"{arr.shape[1]}")
            return arr
        except Exception as e:
            print(f"{e.__class__.__name__}:", e, file=sys.stderr)

    @staticmethod
    def display(df, n):
        """
        - Takes a pandas.DataFrame and an integer as arguments,
        - Displays the first n rows of the dataset if n is positive,
            or the last n rows if n is negative.
        """
        if isinstance(df, pd.DataFrame) and isinstance(n, int):
            if n > 0:
                print(df.head(n))
            else:
                print(df.tail(-n))
