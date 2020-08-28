class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0 and n%2 == 0:
            temp = self.myPow(x, n/2)
            return temp * temp
        
        elif n > 0 and n%2 == 1:
            temp = self.myPow(x, n//2)
            return temp * temp * x
        
        else:
            return 1/self.myPow(x, -n) 
 
