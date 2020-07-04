class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_ind = [ind for ind, x in enumerate(nums) if x%2==1]
        # print(odd_ind)
        c = 0
        if len(odd_ind) < k:
            return 0
        else:
            for ind, x in enumerate(odd_ind[:len(odd_ind)-k+1]):
                if ind == 0:
                    left = x + 1
                else:
                    left = x - odd_ind[ind - 1]
                
                if ind == len(odd_ind)-k:

                    right = len(nums) - odd_ind[ind + k -1]
                else:
                    right = odd_ind[ind + k] - odd_ind[ind + k -1]
                
                c += left * right
                # print(left, right)
            
            return c
        
