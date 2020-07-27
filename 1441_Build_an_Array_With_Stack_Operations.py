class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        ret = []
        ind = 0
        ind_t = 0
        
        num_push = 0
        num_pop = 0
        
        while (num_push - num_pop) < len(target):
            if target[ind_t] == (ind + 1):
                ind_t += 1
                ind += 1
                ret.append('Push')
                num_push += 1
            else:
                ind += 1
                ret.append('Push')
                ret.append('Pop')
                
        return ret
            
