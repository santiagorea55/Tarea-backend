import os
from psycopg.row import dict_row
from dotenv import load_dotenv

#CARGA LAS VARIABLES DEL ARCHIVO
load_dotenv()

DB_HOST= os.get_env("DB_HOST")
DB_PORT= os.get_env("DB_PORT") 
DB_NAME= os.get_env("DB_NAME") 
DB_USER= os.get_env("DB_USER") 
DB_PASSWORD= os.get_env("DB_PASSWORD") 

def get_connection():
    connection = pscopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        password=DB_PASSWORD,
        row_factory=dict_row,
        connect_timeout=5
    )
    return connection