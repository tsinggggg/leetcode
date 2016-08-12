# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        r=int((1+n)/2)
        maxv=n+1
        minv=0

        while (guess(r)!=0):
            if(guess(r)==1):
                minv=r
                r=min(max(int((r+maxv)/2),r+1),maxv-1)
            else:
                maxv=r
                r=max(min(int((r+minv)/2),r-1),minv+1)
        return(r)
        """
        :type n: int
        :rtype: int
        """