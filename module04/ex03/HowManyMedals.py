import pandas as pd


def howManyMedals(df, name):
    if isinstance(df, pd.DataFrame) and isinstance(name, str):
        df = df[(df['Name'] ==                name) & df['Medal'].notna()]
        df = df.loc[:, ['Year', 'Medal']]
        dic = df.groupby(['Year'])['Medal'].apply(list).to_dict()
        for year, value in dic:
            dic[year]