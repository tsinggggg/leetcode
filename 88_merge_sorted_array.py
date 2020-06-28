class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind_m = ind_n = 0
        while ind_n < n:
            curr_n = nums2[ind_n]
            while ind_m < m + ind_n and nums1[ind_m] <= curr_n:
                ind_m += 1

            nums1.insert(ind_m, curr_n)
            ind_m += 1
            nums1.pop(-1)
            ind_n += 1
            
