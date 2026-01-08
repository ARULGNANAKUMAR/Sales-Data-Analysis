import pandas as pd
import random
from datetime import datetime, timedelta

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

df['Total Sales'] = df['Quantity'] * df['Price']

total_revenue = df['Total Sales'].sum()
total_orders = df['Order ID'].nunique()

print("\n Overall Sales Summary")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)

product_sales = df.groupby('Product')['Total Sales'].sum().reset_index()
product_sales = product_sales.sort_values(by='Total Sales', ascending=False)

print("\n Product wise Sales ")
print(product_sales)

category_sales = df.groupby('Category')['Total Sales'].sum().reset_index()
category_sales = category_sales.sort_values(by='Total Sales', ascending=False)

print("\n Category wise Sales")
print(category_sales)

df['Month'] = df['Order Date'].dt.month

monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()

print("\n Monthly Sales Analysis ")
print(monthly_sales)

top_product = product_sales.iloc[0]['Product']
top_category = category_sales.iloc[0]['Category']

print("\n Business Summary")
print(f"Top selling product is {top_product}")
print(f"Best performing category is {top_category}")
print(f"Total revenue generated is {total_revenue}")

df.to_csv("week2_sales_analysis_output.csv", index=False)

print("\n Project completed successfully")
print("week2_sales_analysis_output.csv generated")
