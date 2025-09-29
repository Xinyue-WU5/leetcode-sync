WITH sessions AS (
    SELECT
        session_id,
        MAX(user_id) AS user_id,  -- or MIN(user_id)
        TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) AS session_duration_minutes
    FROM app_events
    GROUP BY session_id
    HAVING TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) >= 30
),
counts AS (
    SELECT
        session_id,
        SUM(CASE WHEN event_type = 'scroll'   THEN 1 ELSE 0 END) AS scroll_count,
        SUM(CASE WHEN event_type = 'click'    THEN 1 ELSE 0 END) AS click_count,
        SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_count
    FROM app_events
    GROUP BY session_id
    HAVING
        (SUM(CASE WHEN event_type = 'click'  THEN 1 ELSE 0 END) * 1.0)
        / NULLIF(SUM(CASE WHEN event_type = 'scroll' THEN 1 ELSE 0 END), 0) < 0.20
        AND SUM(CASE WHEN event_type = 'scroll'   THEN 1 ELSE 0 END) >= 5
        AND SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) = 0
)
SELECT
    s.session_id,
    s.user_id,
    s.session_duration_minutes,
    c.scroll_count
FROM sessions AS s
JOIN counts   AS c
    ON s.session_id = c.session_id
ORDER BY c.scroll_count DESC, s.session_id ASC;