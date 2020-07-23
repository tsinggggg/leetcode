class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        r0, c0 = len(nums), len(nums[0])
        if r0 * c0 != r * c:
            return nums
        
        ret = []
        temp = []
        count = 0
        for i in range(r0):
            for j in range(c0):
                temp.append(nums[i][j])
                count += 1
                
                if count == c:
                    count = 0
                    ret.append(temp.copy())
                    temp.clear()
        return ret
        
