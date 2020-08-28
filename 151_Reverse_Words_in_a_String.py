class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        words = s.split(' ')
        ret = ""
        for x in reversed(words):
            if x.strip() != "":
                ret += x.strip()
                ret += " "
        return ret.strip()
