SELECT
    t1.id,
    CASE
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN COUNT(t2.id) > 0 THEN 'Inner'
        ELSE 'Leaf' END 
        AS type
FROM Tree AS t1 LEFT JOIN Tree AS t2
    ON t2.p_id = t1.id
GROUP BY t1.id, t1.p_id
ORDER BY t1.id;