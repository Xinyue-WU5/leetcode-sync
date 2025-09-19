SELECT 
    ROUND(SUM(a.tiv_2016), 2) AS tiv_2016 
FROM 
    Insurance AS a 
INNER JOIN 
    (SELECT tiv_2015 
        FROM Insurance 
        GROUP BY tiv_2015 
        HAVING COUNT(pid) > 1 
    ) AS b ON a.tiv_2015 = b.tiv_2015 
INNER JOIN 
    (SELECT lat, lon 
        FROM Insurance 
        GROUP BY lat, lon 
        HAVING COUNT(pid) = 1 
    ) AS c ON a.lat = c.lat AND a.lon = c.lon; 