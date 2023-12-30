import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")


customer_data = pd.read_csv('data/customer_data.csv')
booking_data = pd.read_csv('data/booking_data.csv')
destination_data = pd.read_csv('data/destination_data.csv')

booking_data['total_booking_value'] = booking_data['number_of_passengers'] * booking_data['cost_per_passenger']


customer_data.to_csv('data/transformed_customer_data.csv', index=False)
booking_data.to_csv('data/transformed_booking_data.csv', index=False)
destination_data.to_csv('data/transformed_destination_data.csv', index=False)
