class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd = 0
        even = 0
        
        for x in chips:
            if x%2 == 0:
                even += 1
            else:
                odd += 1
                
        return min(odd, even)
