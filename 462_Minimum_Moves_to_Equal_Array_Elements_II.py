class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        l = sorted(nums)
        mid = l[len(l)//2]
        return sum([abs(x - mid) for x in l])
