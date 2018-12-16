class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        dp, incre = [0] * len(A), 1
        for i in range(2, len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]: 
                dp[i] = dp[i-1]+incre
                incre += 1
            else:
                dp[i] = dp[i-1]
                incre = 1
        return dp[-1]
