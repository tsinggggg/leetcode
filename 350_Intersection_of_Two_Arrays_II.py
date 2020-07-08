class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        n1 = 0
        n2 = 0
        
        ret = []
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        while n1 < l1 and n2 < l2:
            
            if nums1[n1] == nums2[n2]:
                ret.append(nums1[n1])
                n1 += 1
                n2 += 1
            elif nums1[n1] > nums2[n2]:
                n2 += 1
            else:
                n1 += 1
        
        
        return ret
