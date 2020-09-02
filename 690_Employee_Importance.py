"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        org = dict()
        imp = dict()
        
        for l in employees:
            org[l.id] = l.subordinates
            imp[l.id] = l.importance
        
        count = 0
        temp_l = [id]
        while temp_l:
            curr = temp_l.pop(0)
            count += imp[curr]
            for leaf in org[curr]:
                temp_l.append(leaf)
        
        return count
        
        
        
