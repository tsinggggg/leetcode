class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        for i in range(len(s)):
            temp_s = set()
            for j in range(i, len(s)):
                if s[j] not in temp_s:
                    temp_s.add(s[j])
                    max_len = max(max_len, j-i +1)
                else:
                    break
        
        return max_len
            
