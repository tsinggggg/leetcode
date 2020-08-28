class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        return max((nums[0] - 1)*(nums[1] - 1), (nums[-1] - 1)*(nums[-2] - 1)) 
