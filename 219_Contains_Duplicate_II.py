class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for ind, x in enumerate(nums):
            if x in d:
                if min([abs(i-ind) for i in d[x]]) <= k:
                    return True
                d[x].append(ind)

            else:
                d[x] = [ind]
        
        return False
        
