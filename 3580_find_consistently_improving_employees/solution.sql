WITH ranked AS (
    SELECT
        pr.employee_id,
        pr.review_date,
        pr.rating,
        ROW_NUMBER() OVER (
        PARTITION BY pr.employee_id
        ORDER BY pr.review_date DESC
        ) AS rn,
        COUNT(*) OVER (PARTITION BY pr.employee_id) AS cnt
    FROM performance_reviews pr
),

last3 AS (
    SELECT
        employee_id,
        MAX(CASE WHEN rn = 1 THEN rating END) AS r1,  
        MAX(CASE WHEN rn = 2 THEN rating END) AS r2,
        MAX(CASE WHEN rn = 3 THEN rating END) AS r3   
    FROM ranked
    WHERE cnt >= 3 AND rn <= 3
    GROUP BY employee_id
),

qualified AS (
    SELECT
        employee_id,
        (r1 - r3) AS improvement_score
    FROM last3
    WHERE r3 IS NOT NULL AND r2 IS NOT NULL
        AND r3 < r2 AND r2 < r1
)

SELECT
    q.employee_id,
    e.name,
    q.improvement_score
FROM qualified q
JOIN employees e
    ON e.employee_id = q.employee_id
ORDER BY q.improvement_score DESC, e.name ASC;