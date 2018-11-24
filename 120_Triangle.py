class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # Bottom up
        if not triangle: return 0
        dp = [[0] * i for i in range(1,len(triangle)+1)]
        dp[-1] = [ _ for _ in triangle[-1]]
        for i in range(len(triangle)-1, 0, -1):
            for j in range(i):
                dp[i-1][j] = min(dp[i][j], dp[i][j+1]) + triangle[i-1][j]
        return dp[0][0]
        
        # Top down
        # if not triangle: return 0
        # dp = [[0] * i for i in range(1,len(triangle)+1)]
        # dp[0][0] = triangle[0][0]
        # for i in range(1, len(triangle)):
        #     for j in range(i+1):
        #         if j == 0: dp[i][j] = dp[i-1][j]+ triangle[i][j]
        #         elif j == i: dp[i][j] = dp[i-1][j-1]+ triangle[i][j]
        #         else: dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1]) + triangle[i][j]
        # return min(dp[-1])
            
