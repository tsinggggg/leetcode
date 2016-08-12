# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        if (n==1):return(1)
        else:
            r=int((1+n)/2)
            minv=0
            maxv=n+1
            while(isBadVersion(r)==isBadVersion(r+1)):
                if(isBadVersion(r)==False):
                    minv=max(r,minv)
                    r=min(maxv-1,max(r+1,int((r+maxv)/2)))
                else:
                    if(r==1):return(r)
                    else:
                        maxv=min(r,maxv)
                        r=max(minv+1,min(r-1,int((r+minv)/2)))
            return(r+1)
        """
        :type n: int
        :rtype: int
        """