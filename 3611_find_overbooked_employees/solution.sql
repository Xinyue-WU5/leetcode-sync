WITH weekly AS (
  SELECT
    m.employee_id,
    YEARWEEK(m.meeting_date, 3) AS yw,         -- ISO week key (Mon–Sun)
    SUM(m.duration_hours) AS week_hours
  FROM meetings AS m
  GROUP BY m.employee_id, YEARWEEK(m.meeting_date, 3)
),
heavy AS (
  SELECT employee_id, yw
  FROM weekly
  WHERE week_hours > 20
),
agg AS (
  SELECT employee_id, COUNT(*) AS meeting_heavy_weeks
  FROM heavy
  GROUP BY employee_id
  HAVING COUNT(*) >= 2
)
SELECT
  a.employee_id,
  e.employee_name,
  e.department,
  a.meeting_heavy_weeks
FROM agg AS a
JOIN employees AS e USING (employee_id)
ORDER BY a.meeting_heavy_weeks DESC, e.employee_name ASC;