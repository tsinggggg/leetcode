class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        
        return 0 if max(A)-min(A) <= 2 * K else max(A)-min(A) - 2 * K
        
        
