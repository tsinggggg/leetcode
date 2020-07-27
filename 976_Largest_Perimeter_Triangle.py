class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        A = sorted(A)
        
        temp = A[-3:]
        candidate = A[:-3]
        
        while not check(temp) and candidate:
            temp.pop(-1)

            temp.insert(0, candidate.pop(-1))

            
        
        if check(temp):
            return sum(temp)
        else:
            return 0
            
        
def check(l):
    return l[0] + l[1] > l[2]
