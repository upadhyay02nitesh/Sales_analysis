# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of records to generate
num_records = 100

# List of products
products = ['Laptop', 'Smartphone', 'Headphones', 'Keyboard', 'Mouse', 'Monitor']

# Generate random dates within the year 2024
dates = [datetime(2024, 1, 1) + timedelta(days=random.randint(0, 364)) for _ in range(num_records)]
print(dates)
# Random product choices for each record
product_choices = [random.choice(products) for _ in range(num_records)]

# Random quantities sold (1 to 10 units per sale)
quantities = np.random.randint(1, 10, num_records)

# Random prices between $50 and $1500 per unit, rounded to 2 decimal places
prices = np.random.uniform(50, 1500, num_records).round(2)

# Create DataFrame for sales data
df_sales = pd.DataFrame({
    'Date': dates,
    'Product': product_choices,
    'Quantity': quantities,
    'Price': prices
})

# Save the sample sales data to a CSV file
df_sales.to_csv('sales_data.csv', index=False)
print("Sample sales data created successfully and saved as 'sales_data.csv'.")
