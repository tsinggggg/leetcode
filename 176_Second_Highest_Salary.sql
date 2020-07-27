# Write your MySQL query statement below
select max(Salary) as SecondHighestSalary from
(select * from Employee
where Salary not in 
(select max(Salary) from Employee) 
) t2;

# SELECT
#     (SELECT DISTINCT
#             Salary
#         FROM
#             Employee
#         ORDER BY Salary DESC
#         LIMIT 1 OFFSET 1) AS SecondHighestSalary
# ;


