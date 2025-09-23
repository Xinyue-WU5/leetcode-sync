SELECT
    e.user_id AS buyer_id,
    e.join_date,
    COALESCE(d.orders_in_2019,0) AS orders_in_2019
FROM Users AS e
LEFT JOIN (SELECT
        b.buyer_id,
        a.join_date,
        COUNT(b.item_id) AS orders_in_2019
    FROM Users AS a LEFT JOIN Orders AS b ON a.user_id = b.buyer_id AND YEAR(b.order_date) = '2019'
            LEFT JOIN Items AS c ON b.item_id = c.item_id 
    GROUP BY b.buyer_id) AS d ON e.user_id = d.buyer_id;