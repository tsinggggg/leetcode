class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind_s = 0
        ind_t = 0
        
        if len(s) > len(t):
            return False
        
        while ind_s < len(s):
            curr = s[ind_s]
            while ind_t < len(t):
                if t[ind_t] == curr:
                    ind_s += 1
                    ind_t += 1
                    break
                else:
                    ind_t += 1
                    
            if ind_t == len(t) and ind_s < len(s):
                return False
        
        if ind_s == len(s):
            return True
        else:
            return False
        
