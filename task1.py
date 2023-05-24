import pandas as pd

"""
Given dataset describes 5-star rating, a movie recommendation service.
The data are contained in the files 'movies.csv' and 'ratings.csv'.
Determine which movie received the most 5.0 ratings.
"""

df_ratings = pd.read_csv('ratings.csv')
df_movies = pd.read_csv('movies.csv', index_col='movieId')  # column 'movieId' as index of DataFrame

rating_5 = df_ratings[df_ratings.rating == 5.0]  # separate the movies with rating 5.0

best_movieId = rating_5['movieId'].value_counts() \
    .index[0]  # index('movieId') of first row as max value after grouping by 'movieId' and count aggregation

movie_name = df_movies[df_movies.index == best_movieId].title

print(movie_name)
