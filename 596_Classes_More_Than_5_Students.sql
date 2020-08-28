# Write your MySQL query statement below
select t1.class from

(select c.class, count(distinct c.student) as s
from courses c
group by class
having s>=5) t1
;
