a)

WITH cte AS (
    SELECT NAME, SALARY,
        RANK() OVER (ORDER BY SALARY) rnk_min,
        RANK() OVER (ORDER BY SALARY DESC) rnk_max
    FROM employee
)

SELECT NAME, SALARY
FROM cte
WHERE rnk_min = 1 OR rnk_max = 1
ORDER BY SALARY;


b)

SELECT emp_dept, COUNT(*)
  FROM emp_details
  GROUP BY emp_dept;
  
  
  output
  
  emp_dept		count
27			2
57			5
47			3
63			3


c)

SELECT SUBSTRING(first_name,1,3) 
     FROM employees;