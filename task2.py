import pandas as pd

"""
Calculate the total consumption of the Baltic countries (Latvia, Lithuania and Estonia)
of categories 4, 12 and 21 for the period from 2005 to 2010 using the power.csv file.
Do not include negative quantities in your calculations.
"""

df = pd.read_csv('power.csv')

df['isBaltic'] = df['country'].isin(['Lithuania', 'Latvia', 'Estonia'])
df['validCategory'] = (df['category'] == 4) | (df['category'] == 12) | (df['category'] == 21)
df['validYear'] = (df['year'] >= 2005) & (df['year'] <= 2010)

df.query('isBaltic and validCategory and validYear', inplace=True)

result = df['quantity'].apply(lambda x: 0. if x < 0 else x).sum()  # replace negative values with 0
print(result)

