import os
from psycopg.rows import dict_row
from dotenv import load_dotenv

#CARGA LAS VARIABLES DEL ARCHIVO
load_dotenv()

DB_HOST= os.getenv("DB_HOST")
DB_PORT= os.getenv("DB_PORT") 
DB_NAME= os.getenv("DB_NAME") 
DB_USER= os.getenv("DB_USER") 
DB_PASSWORD= os.getenv("DB_PASSWORD") 

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