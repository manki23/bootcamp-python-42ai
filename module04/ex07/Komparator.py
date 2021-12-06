import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Komparator:
    def __init__(self, df: pd.DataFrame):
        if isinstance(df, pd.DataFrame):
            self.df = df
        else:
            print("InputError: <df> must be a pandas.DataFrame dataset",
                  file=sys.stderr)
            sys.exit()

    def check_args(self, categorical_var, numerical_var):
        return (
            isinstance(categorical_var, str) and
            isinstance(numerical_var, str) and
            categorical_var in self.df.columns and
            numerical_var in self.df.columns and
            # check if the column data type is numeric
            # (i for integer, u for unsigned integer and f for float)
            self.df[numerical_var].dtype.kind in 'iuf'
        )

    def get_data(self, categorical_var, numerical_var):
        data = self.df[self.df[categorical_var].notna()]
        data = data.pivot(columns=categorical_var, values=numerical_var)
        return data

    def compare_box_plots(self, categorical_var, numerical_var):
        """
        Displays a box plot with several boxes to compare how the distribution
        of the numerical variable changes if we only consider the subpopulation
        which belongs to each category.
        There should be as many boxes as categories.
        For example, with Sex and Height, we would compare the height
        distributions of men vs. women with two boxes on the same graph
        """
        if self.check_args(categorical_var, numerical_var):
            self.df.boxplot(column=numerical_var, by=categorical_var)
            plt.show()

    def density(self, categorical_var, numerical_var):
        """
        Displays the density of the numerical variable. Each subpopulation
        should be represented by a separate curve on the graph
        """
        if self.check_args(categorical_var, numerical_var):
            data = self.get_data(categorical_var, numerical_var)
            data.plot.density(subplots=True)
            plt.xlabel(numerical_var)
            plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        """
        Plots the numerical variable in a separate histogram for each category.
        As an extra, you can use overlapping histograms with a color code
        (but no extra point will be granted!)
        """
        if self.check_args(categorical_var, numerical_var):
            data = self.get_data(categorical_var, numerical_var)
            data.plot.hist(subplots=True)
            plt.xlabel(numerical_var)
            plt.show()
