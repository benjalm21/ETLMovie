### main.py
from extract import extract_movies_from_api
from transform import clean_movies, calculate_popularity_metrics
from load import load_to_mssql
from config import API_KEY

# 1. Extract
from config import API_KEY

def main():
    # Usar la API key
    print(f"API Key cargada: {API_KEY}")

if __name__ == "__main__":
    main()
df_raw = extract_movies_from_api( {API_KEY}, num_pages=3)

# 2. Transform
df_clean = clean_movies(df_raw)
df_metrics = calculate_popularity_metrics(df_clean)

# 3. Load a MS SQL Server
server = 'LAP-BEN'  # Cambia esto si usas un servidor distinto
database = 'MoviesDB'  # Asegúrate que la base de datos exista

load_to_mssql(df_clean, server, database, 'clean_movies')
load_to_mssql(df_metrics, server, database, 'popularity_metrics')

print("ETL completed successfully.")
