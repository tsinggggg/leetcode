class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for x in nums:
            if x in counter.keys():
                counter[x] += 1
            else:
                counter[x] = 0
                
            temp = max(counter.keys(), key=lambda x: counter[x])
            
            if max(counter.values()) >= int(len(nums)/2):
                return temp
