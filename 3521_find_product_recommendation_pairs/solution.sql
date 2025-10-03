WITH pairs AS (
    SELECT
        p1.product_id AS product1_id,
        p2.product_id AS product2_id,
        COUNT(DISTINCT p1.user_id) AS customer_count
    FROM ProductPurchases p1
    JOIN ProductPurchases p2
        ON p1.user_id = p2.user_id
    AND p1.product_id < p2.product_id
    GROUP BY
        p1.product_id, p2.product_id
    HAVING
        COUNT(DISTINCT p1.user_id) >= 3
)
SELECT
    pr.product1_id,
    pr.product2_id,
    i1.category AS product1_category,
    i2.category AS product2_category,
    pr.customer_count
FROM pairs AS pr
JOIN ProductInfo i1 ON i1.product_id = pr.product1_id
JOIN ProductInfo i2 ON i2.product_id = pr.product2_id
ORDER BY
    pr.customer_count DESC,
    pr.product1_id ASC,
    pr.product2_id ASC;