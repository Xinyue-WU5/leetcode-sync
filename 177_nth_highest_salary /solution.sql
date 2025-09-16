-- LIMIT off, 1 is equivalent to LIMIT 1 OFFSET off 
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT 
BEGIN 
  DECLARE off INT DEFAULT N - 1; 
  RETURN ( 
    SELECT DISTINCT salary 
    FROM Employee 
    ORDER BY salary DESC 
    LIMIT off, 1 
  ); 
END; 