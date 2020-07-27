class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        record = set()
        ret = []
        
        for i in range(len(s) - 9):

            temp = s[i : (i+10)]

            if temp in record:
                ret.append(temp)
            else:
                record.add(temp)
                
        return list(set(ret))
        
