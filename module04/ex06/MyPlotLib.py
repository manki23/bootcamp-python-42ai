import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib:
    def __init__(self):
        pass

    @staticmethod
    def check_args(data, features):
        return (
            isinstance(data, pd.DataFrame) and
            isinstance(features, list) and
            all(isinstance(name, str) for name in features) and
            all(name in data.columns for name in features) and
            # if the column data type is numeric
            # (i for integer, u for unsigned integer and f for float)
            all(data[name].dtype.kind in 'iuf' for name in features)
        )

    @staticmethod
    def histogram(data, features):
        """
        Plots one histogram for each numerical feature in the list.
        """
        if MyPlotLib.check_args(data, features):
            data[features].hist()
            plt.show()

    @staticmethod
    def density(data, features):
        """
        plots the density curve of each numerical feature in the list.
        """
        if MyPlotLib.check_args(data, features):
            data[features].plot.kde()
            plt.show()

    @staticmethod
    def pair_plot(data, features):
        """
        Plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.
        """
        if MyPlotLib.check_args(data, features):
            sns.pairplot(data[features])
            plt.show()

    @staticmethod
    def box_plot(data, features):
        """
        Displays a box plot for each numerical variable in the dataset.
        """
        if MyPlotLib.check_args(data, features):
            data[features].plot.box()
            plt.show()
