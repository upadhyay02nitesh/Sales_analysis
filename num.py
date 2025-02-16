# Import necessary libraries
import pandas as pd
import numpy as np

# Load the sales data
df_sales = pd.read_csv('sales_data.csv')

# Convert 'Date' to datetime format
df_sales['Date'] = pd.to_datetime(df_sales['Date'])

# Calculate Total Sales for each transaction
df_sales['Total Sales'] = df_sales['Quantity'] * df_sales['Price']

# 1. Total Sales by Product
total_sales_product = df_sales.groupby('Product')['Total Sales'].sum().reset_index().sort_values(by='Total Sales', ascending=False)
print("Total Sales by Product:")
print(total_sales_product)

# 2. Average Sales per Product
average_sales_product = df_sales.groupby('Product')['Total Sales'].mean().reset_index().sort_values(by='Total Sales', ascending=False)
print("\nAverage Sales per Product:")
print(average_sales_product)

# 3. Top-Selling Products by Quantity
top_selling_products = df_sales.groupby('Product')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
print("\nTop-Selling Products by Quantity:")
print(top_selling_products)

# 4. Monthly Sales Trend
df_sales['Month'] = df_sales['Date'].dt.to_period('M')
monthly_sales_trend = df_sales.groupby('Month')['Total Sales'].sum().reset_index()
monthly_sales_trend['Month'] = monthly_sales_trend['Month'].astype(str)  # Convert to string for better display

print("\nMonthly Sales Trend:")
print(monthly_sales_trend)

# 5. Total Revenue and Average Order Value
total_revenue = np.sum(df_sales['Total Sales'])
average_order_value = np.mean(df_sales['Total Sales'])

print(f"\nTotal Revenue: ${total_revenue:.2f}")
print(f"Average Order Value: ${average_order_value:.2f}")

# 6. Save Analysis Report to CSV
# Combine multiple analysis results into one report
sales_report = total_sales_product.merge(average_sales_product, on='Product', suffixes=('_Total', '_Average'))
sales_report = sales_report.merge(top_selling_products, on='Product')
sales_report.columns = ['Product', 'Total Sales', 'Average Sales', 'Total Quantity Sold']

# Save the combined report to a CSV file
sales_report.to_csv('sales_report.csv', index=False)
print("\nSales report saved to 'sales_report.csv'.")
