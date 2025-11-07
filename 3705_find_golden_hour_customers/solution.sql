WITH a AS
(SELECT
    customer_id,
    SUM(CASE WHEN order_rating IS NOT NUll THEN 1 ELSE 0 END) AS nratedorder,
    COUNT(customer_id) AS total_orders,
    SUM(CASE WHEN ((TIME(order_timestamp)>='11:00:00' AND TIME(order_timestamp)<='14:00:00') OR (TIME(order_timestamp)>='18:00:00'AND TIME(order_timestamp)<='21:00:00')) THEN 1 ELSE 0 END) as ngoldh,
    ROUND(AVG(order_rating),2) as average_rating
FROM restaurant_orders
GROUP BY customer_id
HAVING COUNT(customer_id)>=3 AND ROUND(AVG(order_rating),2)>=4.0)

SELECT
    customer_id,
    total_orders,
    ROUND(100*ngoldh/a.total_orders,0) AS peak_hour_percentage,
    average_rating
FROM a
WHERE (a.ngoldh>=0.6*a.total_orders) AND (a.nratedorder>=0.5*a.total_orders)
ORDER BY average_rating DESC, customer_id DESC;