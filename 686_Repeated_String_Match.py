class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(B) % len(A) == 0:
            times = len(B) // len(A) 
        else:
            times = len(B) // len(A) + 1
        
        if B in A * times:
            return times
        if B in A * (times+1):
            return times + 1
        else:
            return -1
