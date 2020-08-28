class Solution:
    def customSortString(self, S: str, T: str) -> str:
        
        temp = ''.join([x for x in S if x in T])
        
        counter = Counter(T)
        
        for x, c in counter.items():
            if x in temp:
                temp = temp.replace(x, x * c)
            else:
                temp += x*c
        
        
        return temp
        
