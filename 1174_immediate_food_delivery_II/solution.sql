SELECT
    ROUND(100*SUM(a.imme)/COUNT(a.delivery_id),2) AS immediate_percentage
FROM (SELECT
        delivery_id,
        RANK() OVER(PARTITION BY customer_id ORDER BY order_date ASC)  AS rk,
        (CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) AS imme  
    FROM Delivery) AS a
WHERE a.rk = 1;