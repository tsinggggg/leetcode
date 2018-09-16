class Solution(object):
    def isPowerOfThree(self, n):
        if ((n==1)|(n==3)):
            return True
        else:
            if (n<1):
                return False
            else:
                temp=n%3
                if(temp==0):
                    return self.isPowerOfThree(n/3)
                else:
                    return False
        """
        :type n: int
        :rtype: bool
        """

class Solution(object):
    def isPowerOfThree(self, n):
        if ((n==1)|(n==3)):
            return True
        else:
            if (n<1):
                return False
            else:
                temp=n%3
                if(temp==0):
                    return self.isPowerOfThree(n/3)
                else:
                    return False
        """
        :type n: int
        :rtype: bool
        """
        