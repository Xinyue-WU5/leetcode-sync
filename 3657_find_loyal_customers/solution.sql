WITH a AS
(SELECT
    customer_id
FROM customer_transactions
WHERE transaction_type='purchase'
GROUP BY customer_id
HAVING COUNT(customer_id)>=3
),

b AS
(SELECT
    p.customer_id
FROM customer_transactions AS p
INNER JOIN a ON p.customer_id=a.customer_id
GROUP BY p.customer_id
HAVING DATEDIFF(MAX(transaction_date),MIN(transaction_date))>=30
),

d AS
(SELECT
    q.customer_id,
    COUNT(q.transaction_type) AS npurchase
FROM customer_transactions AS q
INNER JOIN b ON q.customer_id=b.customer_id
WHERE q.transaction_type='purchase'
GROUP BY q.customer_id
),

e AS
(SELECT
    z.customer_id,
    COUNT(z.transaction_type) AS nrefund
FROM customer_transactions AS z
INNER JOIN b ON z.customer_id=b.customer_id
WHERE z.transaction_type='refund'
GROUP BY z.customer_id
)

SELECT
    d.customer_id
FROM d
LEFT JOIN e ON d.customer_id=e.customer_id
WHERE (IFNULL(e.nrefund, 0) * 1.0)/ (IFNULL(e.nrefund, 0) + d.npurchase) < 0.2
ORDER BY customer_id ASC