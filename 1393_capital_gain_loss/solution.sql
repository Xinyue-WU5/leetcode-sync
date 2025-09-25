SELECT
    DISTINCT c.stock_name,
    COALESCE(a.plus,0) + COALESCE(b.minus,0) AS capital_gain_loss
FROM Stocks AS c
LEFT JOIN (SELECT
    stock_name,
    sum(price) as plus
FROM Stocks
WHERE operation = 'Sell'
GROUP BY stock_name) AS a
ON c.stock_name = a.stock_name
LEFT JOIN (SELECT
    stock_name,
    sum(-price) as minus
FROM Stocks
WHERE operation = 'BUY'
GROUP BY stock_name) AS b
ON b.stock_name = a.stock_name


-- SELECT
--   stock_name,
--   SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
-- FROM Stocks
-- GROUP BY stock_name;