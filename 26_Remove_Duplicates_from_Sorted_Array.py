class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        ind = 1
        while ind < len(nums):
            
            if nums[ind] == nums[ind - 1]:
                nums.pop(ind)
            else:
                ind += 1
                
        return len(nums)
