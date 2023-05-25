import pandas as pd

"""
Write a function that classifies movies from 'ratings.csv'.
Record the classification result in the 'class' column. 
Note that the classify() method works much faster than the classify_films() method.
"""


def classify_films(row):
    """Takes a row of DataFrame, classifies the movie's rating according to the rules:
        rating 2 and below - low;
        rating 4 and below - medium;
        rating 4.5 and 5 - high.
    Records the result of the classification in the new column 'class'.
    Returns the modified row.
     """
    if row['rating'] >= 4.5:
        row['class'] = 'high'
    elif row['rating'] > 2:
        row['class'] = 'medium'
    else:
        row['class'] = 'low'
    return row


def classify(rating):
    """Takes a value of the movie's rating, classifies it according to the rules:
        rating 2 and below - low;
        rating 4 and below - medium;
        rating 4.5 and 5 - high.
    Returns the result of the classification as a string.
    """
    if rating >= 4.5:
        return 'high'
    elif rating > 2:
        return 'medium'
    else:
        return 'low'


def main():
    df = pd.read_csv('ratings.csv')
    df['class'] = df['rating'].apply(classify)
    print(df.head())


main()
