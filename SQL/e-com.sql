SELECT * FROM `e-commercebusinessanalytics`.`e-com(cleaned_ecommercedataset)`;

#Total Unique Customer
select count(distinct(customer_id)) as Total_Customer from `e-com(cleaned_ecommercedataset)`;

#Total Order
select count(order_id) as Total_Order from `e-com(cleaned_ecommercedataset)`;

#Total Category
select count(distinct(category)) as Total_category from `e-com(cleaned_ecommercedataset)`;

#Total Revenue
select sum(order_value) as Total_revenue from `e-com(cleaned_ecommercedataset)`;

#highest selling product
select product_name,count(quantity) from `e-com(cleaned_ecommercedataset)` group by product_name limit 1;

#highest payment method used 
select payment_method,count(order_value) as Maximum_used_payment_method from `e-com(cleaned_ecommercedataset)` group by payment_method order by payment_method desc limit 1;

#top 10 highest order values
select order_id,max(order_value) as highest_order_value from `e-com(cleaned_ecommercedataset)` group by order_id limit 10;

#category wise total orders
select category,count(order_id) as Total_orders from `e-com(cleaned_ecommercedataset)` group by category;

#Average revenue 
select avg(order_value) as avg_revenue from `e-com(cleaned_ecommercedataset)`;

#Top 10 customers by orders
select customer_id,count(quantity) as customer_order from `e-com(cleaned_ecommercedataset)` group by customer_id limit 10;

#city wise revenue
select city,sum(order_value) as Total_Revenue from `e-com(cleaned_ecommercedataset)` group by city;

#month wise revenue 
select month(order_date_new) as monthly , sum(order_value) as Total_revenue from `e-com(cleaned_ecommercedataset)` group by month(order_date_new) order by month(order_date_new);

#year wise revenue
select year(order_date_new)  as yearly,sum(order_value) as Total_revenue from `e-com(cleaned_ecommercedataset)` group by year(order_date_new) order by year(order_date_new);

#daily revenue
select day(order_date_new)  as daily,sum(order_value) as Total_revenue from `e-com(cleaned_ecommercedataset)` group by day(order_date_new) order by day(order_date_new);

#lowest Sales day
select day(order_date_new)  as daily,min(order_value) as lowest_sales from `e-com(cleaned_ecommercedataset)` group by day(order_date_new) order by day(lowest_sales) desc limit 1;

#average daily revenue
select day(order_date_new)  as daily,avg(order_value) as avg_revenue from `e-com(cleaned_ecommercedataset)` group by day(order_date_new) order by day(order_date_new);

#order place on weekends
select * from `e-com(cleaned_ecommercedataset)` where dayname(order_date_new) in ('Saturday','Sunday');

#order place on weekdays
select * from `e-com(cleaned_ecommercedataset)` where dayname(order_date_new) in ('Monday','Tuesday','Wednesday','Thursday','Friday');

#Top 3 products in each category
select product_name,sum(quantity) as highest_QTY ,category, dense_rank() over(partition by category order by sum(quantity) desc) as ranking  from `e-com(cleaned_ecommercedataset)` group by product_name,category limit 3;

#top 5 customers in each city
select customer_id,sum(quantity) as highest_QTY ,city, dense_rank() over(partition by city order by sum(quantity) desc) as ranking  from `e-com(cleaned_ecommercedataset)` group by customer_id,city limit 5;

#repeat customers
select count(*) as repeated_customers
from
(
 select customer_id
 from `e-com(cleaned_ecommercedataset)`
 group by customer_id
 having count(distinct order_id)>1)t;
 

 