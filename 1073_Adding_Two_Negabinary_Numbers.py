class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        longer, ret = (1, arr1) if len(arr1) > len(arr2) else (2, arr2)
        
        ind1, ind2 = len(arr1) - 1, len(arr2) -1
        
        if longer == 1:
            while ind2 >= 0:
                ret[ind1] += arr2[ind2]
                ind1 -= 1
                ind2 -= 1
        else:
            while ind1 >= 0:
                ret[ind2] += arr1[ind1]
                ind1 -= 1
                ind2 -= 1
                
        
        ind = len(ret) - 1
        handled = 0
        
        while handled<len(ret):

            if ret[ind] in [0,1]:
                handled += 1
                ind -= 1
                continue
            elif ret[ind] > 1:
                
                if ret[ind] % 2 == 0:
                    res = ret[ind] / 2
                    ret[ind] = 0

                    if ind > 0:
                        ret[ind-1] -= res
                    else:
                        ret.insert(0, -res)
                else:
                    res = ret[ind] // 2
                    ret[ind] = 1
                    if ind > 0:
                        ret[ind-1] -= res
                    else:
                        ret.insert(0,-res)
                        
            elif ret[ind] < 0:
                
                if abs(ret[ind]) % 2 == 0:
                    res = abs(ret[ind]) / 2
                    ret[ind] = 0
                    if ind >0:
                        ret[ind-1] += res
                    else:
                        ret.insert(0,res)
                        
                else:
                    res = abs(ret[ind]) // 2 + 1
                    ret[ind] = 1
                    if ind > 0:
                        ret[ind-1] += res
                    else:
                        ret.insert(0, res)
                        
            handled += 1
            ind = len(ret) - handled - 1
            
        ret = [int(x) for x in ret]
        

        while ret[0] == 0 and len(ret) > 1:
            ret.pop(0)
        return ret
                    
                
        
        
