class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ret = set()
        
        d = {l:c for l,c in zip(map(chr, range(ord('a'), ord('z')+1)),
                                  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        
        
        for x in words:
            temp = ""
            for c in x:
                temp += d[c]
            ret.add(temp)
        
        return len(ret)
