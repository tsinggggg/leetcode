class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        # O N
        # for ind in range(len(nums) - 1):
        #     if nums[ind + 1] < nums[ind]:
        #         return nums[ind + 1]
        # return nums[0]
    
        
        # binary search
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2  # when right > left, right > mid
            
            if mid >0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if mid < len(nums) -1 and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]

            
