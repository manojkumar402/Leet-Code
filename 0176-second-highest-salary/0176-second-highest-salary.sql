# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from Employee where salary not in (select max(salary) from Employee);
# SELECT MAX(SALARY) as SecondHighestSalary
# FROM Employee
# WHERE Salary NOT IN (SELECT MAX(Salary)
# FROM Employee)