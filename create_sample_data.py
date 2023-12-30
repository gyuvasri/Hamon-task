import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

customers_data = {
    'customer_id': [1, 2, 3],
    'first_name': ['John', 'Alice', 'Bob'],
    'last_name': ['Doe', 'Smith', 'Johnson'],
    'email': ['john@example.com', 'alice@example.com', 'bob@example.com'],
    'phone': ['123-456-7890', '987-654-3210', '555-123-4567']
}

customers_df = pd.DataFrame(customers_data)

customers_df.to_csv('data/customer_data.csv', index=False)

bookings_data = {
    'booking_id': [101, 102, 103],
    'customer_id': [1, 2, 3],
    'booking_date': ['2023-01-01', '2023-02-15', '2023-03-10'],
    'destination': ['Paris', 'New York', 'Tokyo'],
    'number_of_passengers': [2, 1, 3],
    'cost_per_passenger': [500, 800, 600]
}

bookings_df = pd.DataFrame(bookings_data)

bookings_df.to_csv('data/booking_data.csv', index=False)

destinations_data = {
    'destination_id': [1, 2, 3],
    'destination': ['Paris', 'New York', 'Tokyo'],
    'country': ['France', 'USA', 'Japan'],
    'popular_season': ['Spring', 'Summer', 'Autumn']
}

destinations_df = pd.DataFrame(destinations_data)

destinations_df.to_csv('data/destination_data.csv', index=False)
