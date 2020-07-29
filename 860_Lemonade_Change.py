class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x,y,z = 0,0,0
        
        for c in bills:
            flag, x,y,z = change(x,y,z, c)
            if not flag:
                return False
            
        return True
    
    
def change(x,y,z,c):
    if c == 5:
        return True, x+1, y, z
    
    if c == 10:
        
        if x < 1:
            return False, x,y,z
        else:
            return True, x-1, y+1, z
        
    if c == 20:
        if x>=1 and y>=1:
            return True, x-1, y-1, z+1
        elif x>=3 and y<1:
            return True, x-3, y, z+1
        else:
            return False, x,y,z
    
    
