# data/sample_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
np.random.seed(42)

n_customers = 200
n_products = 50
n_sales = 5000

# Customers
customers = pd.DataFrame({
    'CustomerID': range(1, n_customers+1),
    'CustomerName': [f'Customer_{i}' for i in range(1, n_customers+1)],
    'Region': np.random.choice(['North','South','East','West'], n_customers)
})

# Products
products = pd.DataFrame({
    'ProductID': range(1, n_products+1),
    'ProductName': [f'Product_{i}' for i in range(1, n_products+1)],
    'Category': np.random.choice(['A','B','C'], n_products),
    'Price': np.round(np.random.uniform(5, 500, n_products), 2)
})

# Calendar + Sales
start = datetime(2023,1,1)
dates = [start + timedelta(days=int(x)) for x in np.random.uniform(0, 730, n_sales)]
sales = pd.DataFrame({
    'SaleID': range(1, n_sales+1),
    'Date': dates,
    'CustomerID': np.random.choice(customers.CustomerID, n_sales),
    'ProductID': np.random.choice(products.ProductID, n_sales),
    'Quantity': np.random.randint(1,10, n_sales)
})
sales = sales.merge(products[['ProductID','Price']], on='ProductID')
sales['SalesAmount'] = sales['Quantity'] * sales['Price']

# Write CSVs
customers.to_csv('data/customers.csv', index=False)
products.to_csv('data/products.csv', index=False)
sales.to_csv('data/sales.csv', index=False)
print("CSV files saved to data/")
