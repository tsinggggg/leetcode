class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s)<=1:
            return len(s)
        else:
            
            max_len=0
            for ind,letter in enumerate(s):
                temp_set=set(letter)
                for temp_next in s[ind+1:]:
                    if temp_next not in temp_set:
                        temp_set.add(temp_next)
                    else:
                        break
                        
                max_len=max(max_len,len(temp_set))
            
            return max_len
                    
            
            
        