SELECT
    transaction_date,
    (CASE WHEN MOD(COUNT(transaction_id),2)=1 THEN SUM(amount) ELSE 0 END) AS odd_sum,
    (CASE WHEN MOD(COUNT(transaction_id),2)=0 THEN SUM(amount) ELSE 0 END) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;