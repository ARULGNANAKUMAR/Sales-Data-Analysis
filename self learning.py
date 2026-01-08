# WEEK 2 – Sales Data Analysis & Reporting
# Indha project-la sales data create pannrom,
# revenue calculate pannrom,
# product / category / monthly analysis pannrom,
# final business-ready CSV export pannrom

#Required libraries import pannrom
import pandas as pd                    # Data analysis
import random                          # Sample data create panna
from datetime import datetime, timedelta

# STEP 1: Sales Dataset Create pannrom

# Sample products & categories
products = [
    ('Laptop', 'Electronics'),
    ('Mobile', 'Electronics'),
    ('Headphones', 'Electronics'),
    ('Shoes', 'Fashion'),
    ('T-Shirt', 'Fashion'),
    ('Watch', 'Accessories'),
    ('Backpack', 'Accessories'),
    ('Book', 'Education')
]

sales_data = []

# 50+ sales records create pannrom
for i in range(1, 61):
    product, category = random.choice(products)
    quantity = random.randint(1, 5)
    price = random.randint(300, 50000)
    order_date = datetime(2024, random.randint(1, 12), random.randint(1, 28))

    sales_data.append([
        i,
        order_date,
        product,
        category,
        quantity,
        price
    ])

# DataFrame create pannrom
df = pd.DataFrame(sales_data, columns=[
    'Order ID',
    'Order Date',
    'Product',
    'Category',
    'Quantity',
    'Price'
])

print("Dataset created")
print(df.head())
print(df.shape)

# STEP 2: Total Sales Amount calculate panurom
# Quantity * Price = Total Sales
df['Total Sales'] = df['Quantity'] * df['Price']
# STEP 3: Overall Sales Summary
total_revenue = df['Total Sales'].sum()
total_orders = df['Order ID'].nunique()

print("\n--- Overall Sales Summary ---")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)

# STEP 4: Product-wise Sales Analysis
product_sales = df.groupby('Product')['Total Sales'].sum().reset_index()
product_sales = product_sales.sort_values(by='Total Sales', ascending=False)

print("\n--- Product-wise Sales ---")
print(product_sales)

# STEP 5: Category-wise Sales Analysis

category_sales = df.groupby('Category')['Total Sales'].sum().reset_index()
category_sales = category_sales.sort_values(by='Total Sales', ascending=False)

print("\n--- Category-wise Sales ---")
print(category_sales)

# STEP 6: Monthly Sales Analysis

# Order Date-la irundhu month extract pannrom
df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()

print("\n--- Monthly Sales Analysis ---")
print(monthly_sales)

# STEP 7: Business Summary (Text Insight)

top_product = product_sales.iloc[0]['Product']
top_category = category_sales.iloc[0]['Category']

print("\n--- Business Summary ---")
print(f"Top selling product is {top_product}")
print(f"Best performing category is {top_category}")
print(f"Total revenue generated is {total_revenue}")

# STEP 8: Final Output CSV Export

df.to_csv("week2_sales_analysis_output.csv", index=False)

print("\n Project completed successfully")
print("week2_sales_analysis_output.csv generated")

