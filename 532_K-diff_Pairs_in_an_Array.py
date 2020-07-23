class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        i = j = 0
        l = sorted(nums)
        
        count = set()
        
        while j < len(l):
            
            if i == j:
                j += 1
                continue
            
            diff =  l[j] - l[i]
            

            if diff > k:
                i += 1
            elif diff == k:
                count.add((l[i],l[j]))
                i += 1
                
                if i == len(l):
                    return len(count)
            else:
                j += 1
                
        return len(count)
        
