class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1: return 2**31-1
        sign = 1 if dividend * divisor >= 0 else -1
        a, b, res = abs(dividend), abs(divisor), 0
        for i in reversed(range(32)):
            if a>>i >= b:
                a -= b<<i
                res += 1<<i
        return sign * res
