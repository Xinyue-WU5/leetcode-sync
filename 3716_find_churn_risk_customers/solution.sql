WITH a AS
(SELECT
    user_id,
    DATEDIFF(MAX(event_date), MIN(event_date)) AS days_as_subscriber,
    SUM(CASE WHEN event_type='downgrade' THEN 1 ELSE 0 END) AS ndown,
    MAX(event_date) AS lastday,
    MAX(monthly_amount) AS max_historical_amount
FROM subscription_events
GROUP BY user_id
)

SELECT
    b.user_id,
    b.plan_name AS current_plan,
    b.monthly_amount AS current_monthly_amount,
    a.max_historical_amount,
    a.days_as_subscriber
FROM subscription_events AS b
JOIN a on b.user_id=a.user_id AND b.event_date=a.lastday
WHERE (b.plan_name IS NOT NULL) AND (a.ndown>0) AND (b.monthly_amount<0.5*a.max_historical_amount) AND (a.days_as_subscriber>=60)
ORDER BY a.days_as_subscriber DESC, b.user_id ASC;