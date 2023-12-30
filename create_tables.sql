
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    customer_id INT,
    booking_date DATE,
    destination VARCHAR(255),
    number_of_passengers INT,
    cost_per_passenger FLOAT,
    total_booking_value FLOAT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE destinations (
    destination_id SERIAL PRIMARY KEY,
    destination VARCHAR(255),
    country VARCHAR(255),
    popular_season VARCHAR(20)
);
