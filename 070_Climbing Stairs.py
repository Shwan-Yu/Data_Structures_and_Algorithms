class Solution(object):
    def climbStairs(self, n):
        if not n: return 0
        dp1 = dp2 = 1
        for i in range(2, n+1):
            tmp = dp1+dp2; dp1 = dp2; dp2 = tmp
        return dp2
