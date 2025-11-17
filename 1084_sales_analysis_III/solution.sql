WITH a AS(
SELECT
    product_id,
    SUM(CASE WHEN sale_date >= '2019-01-01' AND sale_date <=  '2019-03-31' THEN 0 ELSE 1 END) AS dinr
FROM Sales
GROUP BY product_id
)

SELECT
    a.product_id,
    b.product_name
FROM a
LEFT JOIN Product AS b
ON a.product_id=b.product_id
WHERE a.dinr=0;