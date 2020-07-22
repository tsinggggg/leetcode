class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        if len(nums) % k != 0:
            return False
        
        d = collections.defaultdict(lambda :[])
        nums = sorted(nums)
        
        for ind, i in enumerate(nums):
            d[i].append(ind)
            
        num_of_group = len(nums) // k
        
        keys = sorted(d.keys())
        
        for i in range(num_of_group):

            min_key = keys[0]
            
            if len(keys) < k:
                return False
            else:
                for x in range(k):
                    curr_key = min_key + x
                    if len(d[curr_key]) == 0:
                        return False
                    else:
                        d[curr_key].pop(0)
                        if len(d[curr_key]) == 0:
                            keys.remove(curr_key)
        
        return True
                

        
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
#         if len(nums) % k != 0:
#             return False
        
#         nums = sorted(nums)
#         while len(nums) > 0:
            
#             if not remove_min_k(nums, k):
#                 return False
            
#         return True
    
    
# def remove_min_k(nums, k):
#     n1 = nums.pop(0)
#     counter = 1
#     to_removed = []

#     for i in range(len(nums)):
#         if nums[i] == (n1 + counter):
#             counter += 1
#             to_removed.append(i)
#             if counter == k:
#                 break

#     if counter == k:
#         for x in reversed(to_removed):
#             nums.pop(x)
#         return True
#     else:
#         return False
        
