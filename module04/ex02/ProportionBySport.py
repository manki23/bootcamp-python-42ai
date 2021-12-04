import pandas as pd


def proportionBySport(df, year, sport, gender):
    if (
        isinstance(df, pd.DataFrame) and isinstance(year, int) and
        isinstance(sport, str) and gender in ['F', 'M']
    ):
        df = df[(df['Sex'] == gender) & (df['Year'] == year)]
        return (
            df[df['Sport'] == sport].loc[:, 'Name'].drop_duplicates().count() /
            df.loc[:, 'Name'].drop_duplicates().count()
        )
