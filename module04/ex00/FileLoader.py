import sys
import pandas as pd


class FileLoader:
    def load(path):
        """
        - Takes as an argument the file path of the dataset to load,
        - Displays a message specifying the dimensions of the dataset
            (e.g. 340 x 500)
        - And returns the dataset loaded as a pandas.DataFrame
        """
        try:
            return pd.read_csv(path)
        except Exception as e:
            print(f"{e.__class__.__name__}:", e, file=sys.stderr)
    
    def display(df, n):
        """
        - Takes a pandas.DataFrame and an integer as arguments,
        - Displays the first n rows of the dataset if n is positive,
            or the last n rows if n is negative.
        """
        pass