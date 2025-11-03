# Write your MySQL query statement below
WITH b AS
(SELECT
    driver_id,
    AVG(distance_km/fuel_consumed) AS second_half_avg
FROM trips
WHERE MONTH(trip_date) IN(7,8,9,10,11,12)
GROUP BY driver_id
),

e AS
(SELECT
    a.driver_id,
    c.driver_name,
    AVG(a.distance_km/a.fuel_consumed) AS first_half_avg
FROM trips AS a
INNER JOIN drivers AS c
ON a.driver_id = c.driver_id
WHERE MONTH(trip_date) IN(1,2,3,4,5,6)
GROUP BY driver_id)

SELECT
    e.driver_id,
    e.driver_name,
    ROUND(e.first_half_avg,2) AS first_half_avg,
    ROUND(b.second_half_avg,2) AS second_half_avg,
    ROUND((b.second_half_avg-e.first_half_avg),2) AS efficiency_improvement
FROM e
INNER JOIN b
ON e.driver_id = b.driver_id
WHERE b.second_half_avg > e.first_half_avg
ORDER BY efficiency_improvement DESC, driver_name ASC;