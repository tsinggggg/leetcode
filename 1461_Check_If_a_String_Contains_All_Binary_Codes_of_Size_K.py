class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        map = set()
        for i in range(k, len(s)+1):
            map.add(s[(i - k):i])
        return len(map) == 2**k
        
        
