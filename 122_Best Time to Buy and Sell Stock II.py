class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            prof = prices[i] - prices[i-1]
            if prof > 0: res += prof
        return res
