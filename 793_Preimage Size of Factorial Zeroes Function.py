class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        # n(log5K * log5K)
        # given num find k
        def findK(num):
            fac, count = 5, 0
            while fac <= num:
                count += num // fac
                fac *= 5
            return count
        l, r = 1, 5 * K
        # keep finding until l is the smallest num that have K 0s, because if we have it, then we have 5 of it.
        while l < r:
            mid = (l+r)//2
            find = findK(mid)
            if find == K: return 5
            elif find < K: l = mid + 1
            else: r = mid
        # K 0s may be the right most boundary: K=3, 1,15, can never find 15
        return 5 if findK(l) == K else 0
