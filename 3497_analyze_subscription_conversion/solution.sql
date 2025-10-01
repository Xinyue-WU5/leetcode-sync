WITH a AS
(SELECT
    user_id,
    ROUND(AVG(activity_duration),2) AS paid_avg_duration
FROM UserActivity
WHERE activity_type = 'paid'
GROUP BY user_id), 

b AS
(SELECT
    user_id,
    ROUND(AVG(activity_duration),2) AS trial_avg_duration
FROM UserActivity
WHERE activity_type = 'free_trial'
GROUP BY user_id), 

c AS
(SELECT DISTINCT
    user_id
FROM UserActivity
WHERE activity_type = 'paid')

SELECT
    c.user_id,
    b.trial_avg_duration,
    a.paid_avg_duration
FROM c
LEFT JOIN b ON c.user_id = b.user_id
LEFT JOIN a ON c.user_id = a.user_id
ORDER BY user_id ASC;