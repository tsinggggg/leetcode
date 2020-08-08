class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[-1] * n for x in range(n)]
        
        ind = (0, 0)
        direction = 'right'
        min_row = 0
        max_row = n-1
        min_col = 0
        max_col = n-1
        
        curr = 1
        
        while curr <= n**2:
            ret[ind[0]][ind[1]] = curr
            curr += 1
            
            if direction == 'right':
                if ind[1] + 1 > max_col:
                    direction = 'down'
                    ind = (ind[0] + 1, ind[1])
                    min_row += 1
                else:
                    ind = (ind[0], ind[1] + 1)
            elif direction == 'down':
                
                if ind[0] + 1 > max_row:
                    direction = 'left'
                    ind = (ind[0], ind[1] - 1)
                    max_col -= 1
                else:
                    ind = (ind[0] + 1, ind[1])
            
            elif direction == 'left':
                
                if ind[1] - 1 < min_col:
                    direction = 'up'
                    ind = (ind[0] - 1, ind[1])
                    max_row -= 1
                else:
                    ind = (ind[0], ind[1] - 1)
                    
            elif direction == 'up':
                
                if ind[0] - 1 < min_row:
                    direction = 'right'
                    ind = (ind[0], ind[1] + 1)
                    min_col += 1
                else:
                    ind = (ind[0] - 1, ind[1])
                    
        return ret
            
