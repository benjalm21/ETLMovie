### extract.py
import requests
import pandas as pd

def extract_movies_from_api(api_key, num_pages=20):
    movies = []
    for page in range(1, num_pages + 1):
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={page}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            movies.extend(data['results'])
        else:
            print(f"Error en la página {page}: {response.status_code}")
    return pd.DataFrame(movies)