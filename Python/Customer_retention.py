import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv("C:\\Users\\jeetv\\OneDrive\\Desktop\\data analyst projects\\E-commerce customer retention intelligence plateform\\Ecommercedataset.csv")
print(df)


#Top 5 records
df1=df.head(5)
print(df1)

#Bottom 5 records
df1=df.tail(5)
print(df1)

#Summary of the dataset
df1=df.describe()
print(df1)

#Information about the dataset
df1=df.info()
print(df1)

#Number of rows and columns
df1=df.shape
print(df1)

#Number of null values
df1=df.isnull().sum()
print(df1)

#Filling null values
df1=df['city'].fillna("Anand" ,inplace=True)
print(df1)


df1=df['product_name'].fillna("Nan", inplace=True)
print(df1)

df1=df['order_value'].fillna(df['order_value'].mean(), inplace=True)
print(df1)

df1=df['payment_method'].fillna("UPI", inplace=True)
print(df1)

df1=df.isnull().sum()
print(df1)

#Unique values in the dataset
df1=df.nunique()
print(df1)

#duplicates in the dataset
df1=df.duplicated().sum()
print(df1)

#Removing duplicates
df1=df.drop_duplicates(inplace=True)
print(df1)

#Total Orders
df1=df['order_id'].nunique()
print(df1)

#Total Customers
df1=df['customer_id'].nunique()
print(df1)

#Total Revenue
df1=df['order_value'].sum()
print(df1)

#Most popular product
df1=df['product_name'].value_counts().idxmax()
print(df1)

#Most Unpopular product
df1=df['product_name'].value_counts().idxmin() 
print(df1)

#Most popular payment method
df1=df['payment_method'].value_counts().idxmax()
print(df1)

#Top 5 cities with the highest orders
df1=df.groupby('city')['order_id'].count().sort_values(ascending=False).head(5)
print(df1)

#Top 5 customers with the highest revenue
df1=df.groupby('customer_id')['order_value'].sum().sort_values(ascending=False).head(5)
print(df1)

#Highest Quantity product
df1=df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(1)
print(df1)

df1=df['city']
print(df1)

#revenue by category
df1=df.groupby('category')['order_value'].sum().sort_values(ascending=False)
print(df1)

#Average order value by category
df1=df.groupby('category')['order_value'].mean().sort_values(ascending=False)
print(df1)

#Top 10 products with the highest revenue
df1=df.groupby('product_name')['order_value'].sum().sort_values(ascending=False).head(10)
print(df1)

#Revenue by payment method
df1=df.groupby('payment_method')['order_value'].sum().sort_values(ascending=False) 
print(df1)

#revenue by city
df1=df.groupby('city')['order_value'].sum().sort_values(ascending=False)
print(df1)

#average quantity by category
df1=df.groupby('category')['order_value'].mean().sort_values(ascending=False)
print(df1)



#orders with above average order value
avg = np.mean(df["order_value"])
high_orders = df[df["order_value"] > avg]
print(high_orders.head())

#highest and lowest order values
print("Max Order:", np.max(df["order_value"]))
print("Min Order:", np.min(df["order_value"]))

#Revenue by city visualization
city_revenue = df.groupby('city')['order_value'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
city_revenue.plot(kind='bar')
plt.title('Revenue by City')
plt.xlabel('City')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

#Revenue by category visualization
category_revenue = df.groupby('category')['order_value'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
category_revenue.plot(kind='bar')
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

#Payment method distribution visualization
payment_method=df['payment_method'].value_counts()
plt.figure(figsize=(10,5))
payment_method.plot(kind='line')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

#Top 10 products with the highest revenue visualization
top_products = df.groupby('product_name')['order_value'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))  
top_products.plot(kind='bar')
plt.title('Top 10 Products with the Highest Revenue')
plt.xlabel('Product Name')
plt.ylabel('Revenue')   
plt.xticks(rotation=45)
plt.show()

df.to_csv("C:\\Users\\jeetv\\OneDrive\\Desktop\\data analyst projects\\E-commerce customer retention intelligence plateform\\Cleaned_Ecommercedataset.csv", index=False)


#insights from the dataset
'''1. Havells Fan is the most frequently purchased product on the platform.
    This suggests consistent customer demand and indicates that maintaining adequate inventory levels for this product could help prevent stockouts and lost sales.'''

'''2. Vadodara generates the highest number of orders and revenue among all cities.
    This indicates a strong customer base in the region. The company can prioritize targeted marketing campaigns and customer retention initiatives in Vadodara to maximize revenue growth.
'''

'''3. UPI is the most preferred payment method among customers.
    This highlights the growing adoption of digital payments. Ensuring a fast and reliable UPI checkout experience may help improve customer satisfaction and reduce transaction abandonment.'''

'''4. Electronics generates the highest revenue among all categories.
    This indicates strong customer demand and higher spending in the Electronics segment. The company can focus promotional campaigns and inventory planning around high-performing electronic products.'''

'''5. A small group of customers contributes a significant portion of total revenue.
    Implementing loyalty programs and personalized offers for high-value customers could improve retention and long-term revenue.'''

