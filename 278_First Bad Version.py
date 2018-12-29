# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # mid's value is mid+1
        l, r = 0, n-1
        while l < r:
            mid = (l+r) // 2
            print(l, mid, r)
            res = isBadVersion(mid+1)
            if not res:
                l = mid+1
            else:
                r = mid
        return l+1
