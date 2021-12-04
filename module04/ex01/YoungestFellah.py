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
        women = df[(df['Sex'] == 'F')]
        woman = women.loc[:, ['Age']].min()
        woman_age = woman['Age']
        men = df[(df['Sex'] == 'M')]
        man = men.loc[:, ['Age']].min()
        man_age = man['Age']

    return {'youngest_woman_age': woman_age, 'youngest_man_age': man_age}
