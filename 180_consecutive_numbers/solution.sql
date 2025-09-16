SELECT 
    DISTINCT l1.num AS ConsecutiveNums 
FROM Logs as l1, 
     logs as l2, 
     logs as l3 
WHERE l2.id - l1.id = 1 AND 
      l3.id - l2.id = 1 AND 
      l1.num = l2.num AND 
      l2.num = l3.num;