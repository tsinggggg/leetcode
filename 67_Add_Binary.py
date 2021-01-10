class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = min(len(a), len(b))
        ret = []
        overflow = 0
        
        for ind in range(1, l+ 1):
            if a[-ind] == b[-ind] and a[-ind] == "0" and overflow == 1:
                ret.insert(0, "1")
                overflow = 0
            elif a[-ind] == b[-ind] and a[-ind] == "0" and overflow == 0:
                ret.insert(0, "0")
            elif a[-ind] != b[-ind] and overflow == 0:
                ret.insert(0, "1")
            elif a[-ind] != b[-ind] and overflow == 1:
                ret.insert(0, "0")      
                overflow = 1
            elif a[-ind] == b[-ind] and a[-ind] == "1" and overflow == 1:
                ret.insert(0, "1")      
                overflow = 1  
            elif a[-ind] == b[-ind] and a[-ind] == "1" and overflow == 0:
                ret.insert(0, "0")      
                overflow = 1     
        
        if len(a) != len(b):        
            c = a if len(a) > len(b) else b
            
            for ind in range(l+1, len(c) + 1):
                if c[-ind] == "0" and overflow == 0:
                    ret.insert(0, "0")
                elif c[-ind] == "0" and overflow == 1:
                    ret.insert(0, "1")
                    overflow = 0
                elif c[-ind] == "1" and overflow == 1:
                    ret.insert(0, "0")
                    overflow = 1
                elif c[-ind] == "1" and overflow == 0:
                    ret.insert(0, "1")
                    overflow = 0
        
        if overflow == 1:
            ret.insert(0, "1")
            
        if len(ret) > 1 and ret[0] == "0":
            ret.pop(0)
            
        return "".join(ret)
