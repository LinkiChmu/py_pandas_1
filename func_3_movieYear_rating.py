import pandas as pd

years = list(range(1950, 2011))  # list of years from 1950 to 2010 inclusive


def production_year(movie_title):
    """Identifies the release year from the movie title.
    For each year in the list 'years' checks, if the year is in the movie title, returns that year.
    Otherwise, it returns 1900.
    """
    for year in years:
        if str(year) in movie_title:
            return year
    return 1900


def main():
    movies_df = pd.read_csv('movies.csv')
    ratings_df = pd.read_csv('ratings.csv')

    merged = ratings_df.merge(movies_df, on='movieId', how='left')

    merged['year'] = merged.title.apply(production_year)  # add the column 'year'

    avg_rating_year = merged[['year', 'rating']].groupby('year').mean().sort_values('rating', ascending=False)

    print(avg_rating_year.head(10))


main()
