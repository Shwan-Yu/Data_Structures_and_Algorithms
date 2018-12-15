class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # O(lgN)
        # (start + start + n -1) * (n/2) = N, summation formula
        # start = (2N - n(n-1)) / 2n
        count = 0
        for n in range(1, int((2*N)**0.5) + 1):
            if (2*N - n*(n-1))%(2*n) == 0: count += 1
        return count
