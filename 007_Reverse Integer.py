class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res, sign = 0, 1 
        if x < 0:
            x *= -1; sign = -1
        for char in `x`[::-1]: 
            res = res * 10 + ord(char) - ord("0")
        return sign * res if -2**31<= res<= 2**31-1 else 0
