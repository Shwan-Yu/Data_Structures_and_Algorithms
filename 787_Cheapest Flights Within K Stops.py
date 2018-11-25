class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        if not flights: return 0
        dp = [float("inf")] * n
        dp[src] = 0
        for k in range(K+1):
            dp_cur = dp[:]
            for (a, i, price) in flights:
                dp_cur[i] = min(dp_cur[i], dp[a] + price)
            dp = dp_cur
        return dp[dst] if dp[dst] != float("inf") else -1
