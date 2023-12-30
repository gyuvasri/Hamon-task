import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=db_port
)
cursor = conn.cursor()

# Load data into PostgreSQL
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

cursor.close()
conn.close()
