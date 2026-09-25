-- Write your query below
with order_cte as (
    select customer_id,
        count(*) filter (where product_name = 'A') as order_a,
        count(*) filter (where product_name = 'B') as order_b,
        count(*) filter (where product_name = 'C') as order_c
    from orders
    group by customer_id
)
select c.customer_id, c.customer_name 
from customers c
inner join order_cte oc on oc.customer_id = c.customer_id
where (order_a > 0) and (order_b > 0) and order_c = 0
order by c.customer_name