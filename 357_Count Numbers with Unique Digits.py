class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP: probability: n=1: 9+n0, n=2: 9*9+n1, n=3: 9*9*8 +n2
        prob = [9]+[i for i in range(9,0,-1)]
        res, product = 1, 1
        for i in range(n if n <= 10 else 10):
            product *= prob[i]
            res += product
        return res
