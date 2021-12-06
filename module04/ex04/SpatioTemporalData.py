import sys
import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        if isinstance(df, pd.DataFrame):
            self.df = df
        else:
            print("InputError: <df> must be a pandas.DataFrame dataset",
                  file=sys.stderr)
            sys.exit()

    def when(self, location):
        """
        Takes a location as an argument and returns a list containing the
        years where games were held in the given location
        """
        if isinstance(location, str):
            location_df = self.df[(self.df['City'] == location)]
            year_df = location_df.loc[:, ['Year']].drop_duplicates()
            return year_df.values[..., 0].tolist()

    def where(self, date):
        """
        Takes a date as an argument and returns the location where the
        Olympics took place in the given year
        """
        if isinstance(date, int) and date > 0:
            year_df = self.df[(self.df['Year'] == date)]
            location_df = year_df.loc[:, ['City']].drop_duplicates()
            return location_df.values[..., 0].tolist()
