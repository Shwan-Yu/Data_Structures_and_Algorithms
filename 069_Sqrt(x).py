class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r:
            mid = (l+r)//2
            if mid ** 2 > x:
                r = mid
            else:
                l = mid + 1
        return l-1 if x > 1 else l # 0, 1 corner case
