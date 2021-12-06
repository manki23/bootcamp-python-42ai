import pandas as pd


def howManyMedalsByCountry(df, name):
    if isinstance(df, pd.DataFrame) and isinstance(name, str):
        team_sports = [
            'Basketball',
            'Football',
            'Tug-Of-War',
            'Badminton',
            'Sailing',
            'Handball',
            'Water Polo',
            'Hockey',
            'Rowing',
            'Bobsleigh',
            'Softball',
            'Volleyball',
            'Synchronized Swimming',
            'Baseball',
            'Rugby Sevens',
            'Rugby',
            'Lacrosse',
            'Polo'
        ]
        df = df[df['Team'] == name]
        df = df.loc[:, ['Team', 'Games', 'Year', 'Sport', 'Event', 'Medal']]
        df1 = df[df['Sport'].isin(team_sports)].drop_duplicates()
        df2 = df[~(df['Sport'].isin(team_sports))]
        df = pd.concat([df1, df2])
        df = df.loc[:, ['Year', 'Medal']]
        dic = df.groupby(['Year'])['Medal'].apply(list).to_dict()
        for year, value in dic.items():
            dic[year] = {
                'G': dic[year].count('Gold'),
                'S': dic[year].count('Silver'),
                'B': dic[year].count('Bronze')
            }
        return dic
