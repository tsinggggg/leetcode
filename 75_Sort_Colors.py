class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bottom, curr, top = 0, 0, len(nums) - 1
        while curr <= top:
            if nums[curr] == 0:
                nums[bottom], nums[curr] = nums[curr], nums[bottom]
                curr += 1
                bottom += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[top], nums[curr] = nums[curr], nums[top]
                top -= 1

