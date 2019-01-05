class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # count[i] += count[i-coin_val]
        # count 1 1 1 1 1
        # count 1 1 2 2 3
        # count 1 1 2 2 4
        count = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount+1):
                count[i] += count[i-coin]
        return count[-1]
