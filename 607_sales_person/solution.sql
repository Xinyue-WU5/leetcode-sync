SELECT 
    DISTINCT s.name
FROM SalesPerson AS s
LEFT JOIN Orders AS o
    ON o.sales_id = s.sales_id
LEFT JOIN Company AS c
    ON c.com_id = o.com_id AND c.name = 'RED'
WHERE c.com_id IS NULL;