class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        record = set()
        ret = []

        if n == 1:
            return []
        
        for i in range(2,n+1):
            for j in range(1, i):
                
                if j/i not in record:
                    
                    record.add(j/i)
                    
                    ret.append(str(j) + "/" + str(i))
                    
        return ret
                    
                    
                
                
                
                
                
        
