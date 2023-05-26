import pandas as pd
import re

geo_data = {'Центр': ['москва', 'тула', 'ярославль'],
            'Северо-Запад': ['петербург', 'псков', 'мурманск'],
            'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
            }


def geo_classify(query):
    """For a search query string, defines the geographic belonging to a certain region.
    If the request contains the name of the city of the region, then the function returns the region.
    Otherwise, it returns 'undefined'.
    Rules for distribution by region according to the dictionary 'geo_data'.
    """
    for word in re.findall(r'[а-я]{3,}', query, re.I):
        for region, cities in geo_data.items():
            if word in cities:
                return region
    return 'undefined'


def main():
    df = pd.read_csv('keywords.csv')
    df['region'] = df['keyword'].apply(geo_classify)
    print(df.head())
    print()
    print(df[df['region'] != 'undefined'].head())


main()
