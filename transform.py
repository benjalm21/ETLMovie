### transform.py
import pandas as pd

def clean_movies(df):
    df = df.dropna(subset=['title'])
    df = df.drop_duplicates(subset='title')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['year'] = df['release_date'].dt.year
    return df


def calculate_popularity_metrics(df):
    popularity_by_year = df.groupby('year')['popularity'].mean().reset_index()
    popularity_by_year.columns = ['year', 'avg_popularity']
    return popularity_by_year