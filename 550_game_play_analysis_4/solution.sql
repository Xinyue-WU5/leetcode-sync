SELECT 
    ROUND(COUNT(T2.player_id) / (SELECT COUNT(DISTINCT T1.player_id) FROM Activity T1), 2) AS fraction
FROM 
    (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) AS T1
JOIN 
    Activity AS T2 ON T1.player_id = T2.player_id
    AND DATEDIFF(T2.event_date, T1.first_login) = 1; 