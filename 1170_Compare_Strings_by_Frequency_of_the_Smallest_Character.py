class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            c = min(list(s))
            return len([x for x in s if x == c])
        q = [f(x) for x in queries]
        w = [f(x) for x in words]
        return [len([y for y in w if x < y]) for x in q ]
