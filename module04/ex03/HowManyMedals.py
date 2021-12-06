import pandas as pd


def howManyMedals(df, name):
    if isinstance(df, pd.DataFrame) and isinstance(name, str):
        df = df[(df['Name'] == name)]
        df = df.loc[:, ['Year', 'Medal']]
        dic = df.groupby(['Year'])['Medal'].apply(list).to_dict()
        for year, value in dic.items():
            dic[year] = {
                'G': dic[year].count('Gold'),
                'S': dic[year].count('Silver'),
                'B': dic[year].count('Bronze')
            }
        return dic
