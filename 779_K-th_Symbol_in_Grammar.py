class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        
        num_elements = 2 ** (N - 1)
        if K <= num_elements/2:
            return self.kthGrammar(N-1, K)
        else:
            return 1 - self.kthGrammar(N-1, K - num_elements/2)
        
