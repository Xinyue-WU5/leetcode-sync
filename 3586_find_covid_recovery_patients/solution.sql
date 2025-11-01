SELECT
    a.patient_id,
    c.patient_name,
    c.age,
    DATEDIFF(min(b.test_date),min(a.test_date)) AS recovery_time
FROM covid_tests AS a
INNER JOIN covid_tests AS b
ON a.patient_id=b.patient_id
    AND a.test_date<b.test_date
    AND a.result='Positive'
    AND b.result='Negative'
INNER JOIN patients AS c
ON a.patient_id=c.patient_id
GROUP BY a.patient_id, c.patient_name, c.age
ORDER BY recovery_time,patient_name ASC;