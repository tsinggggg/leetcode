class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros = [x for x in range(len(nums)) if nums[x] == 0]
        zeros = [-1] + zeros + [len(nums)]
        
        temp = 0
        for x in range(len(zeros) - 1):
            temp = max(temp, zeros[x+1]-zeros[x] - 1)
        
        return temp
        
        
