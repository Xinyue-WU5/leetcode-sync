WITH a AS
(SELECT
    store_id,
    MAX(price) AS highestprice,
    MIN(price) AS lowestprice
FROM inventory
GROUP BY store_id
HAVING COUNT(product_name)>=3
),

b AS
(
SELECT
    p.store_id,
    p.product_name AS most_exp_product,
    p.quantity
FROM inventory AS p
INNER JOIN a
ON p.store_id=a.store_id AND p.price=a.highestprice
),

c AS
(
SELECT
    q.store_id,
    q.product_name AS cheapest_product,
    q.quantity
FROM inventory AS q
INNER JOIN a
ON q.store_id=a.store_id AND q.price=a.lowestprice
)


SELECT
    b.store_id,
    d.store_name,
    d.location,
    b.most_exp_product,
    c.cheapest_product,
    ROUND(c.quantity/b.quantity,2) AS imbalance_ratio
FROM b
LEFT JOIN c ON b.store_id=c.store_id AND b.quantity<c.quantity
LEFT JOIN stores AS d ON b.store_id=d.store_id
ORDER BY imbalance_ratio DESC, store_name ASC;