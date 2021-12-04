import pandas as pd


def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    man_age = float("NaN")
    woman_age = float("NaN")
    if isinstance(df, pd.DataFrame) and isinstance(year, int):
        df = df[df['Year'] == year]
        woman_age = df[(df['Sex'] == 'F')].loc[:, ['Age']].min()['Age']
        man_age =  df[(df['Sex'] == 'M')].loc[:, ['Age']].min()['Age']

    return {'f': woman_age, 'm': man_age}
