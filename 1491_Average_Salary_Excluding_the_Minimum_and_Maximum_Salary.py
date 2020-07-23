class Solution:
    def average(self, salary: List[int]) -> float:
        max_s = max(salary)
        min_s = min(salary)
        
        return (sum(salary) - max_s - min_s)/(len(salary) - 2)
