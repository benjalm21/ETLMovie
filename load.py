### load.py
import pyodbc
import pandas as pd

def load_to_mssql(df, server, database, table_name):
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};DATABASE={database};Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Elimina la tabla si existe
    cursor.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name};")
    conn.commit()

    # Crea la tabla automáticamente desde el DataFrame
    cols = ", ".join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
    cursor.execute(f"CREATE TABLE {table_name} ({cols});")
    conn.commit()

    # Insertar los datos
    for index, row in df.iterrows():
        values = ", ".join([f"'{str(value).replace("'", "''")}'" for value in row])
        cursor.execute(f"INSERT INTO {table_name} VALUES ({values});")
    conn.commit()
    cursor.close()
    conn.close()