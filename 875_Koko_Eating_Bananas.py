class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        temp = max(sum(piles) // H, 1)

        while True:
            
            count = 0
            for x in piles:
        
                if x % temp == 0:
                    count += x/temp
                else:
                    count += x//temp + 1
            
            if count <= H:
                return temp
            else:
                temp += 1
        
