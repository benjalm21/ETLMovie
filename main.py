### main.py
from extract import extract_movies_from_api
from transform import clean_movies, calculate_popularity_metrics
from load import load_to_mssql
from config import API_KEY

# 1. Extract
api_key = '1fc907c2d888abe7cd75fb78250c8805'
df_raw = extract_movies_from_api(api_key, num_pages=3)

# 2. Transform
df_clean = clean_movies(df_raw)
df_metrics = calculate_popularity_metrics(df_clean)

# 3. Load a MS SQL Server
server = 'LAP-BEN'  # Cambia esto si usas un servidor distinto
database = 'MoviesDB'  # Asegúrate que la base de datos exista

load_to_mssql(df_clean, server, database, 'clean_movies')
load_to_mssql(df_metrics, server, database, 'popularity_metrics')

print("ETL completed successfully.")
