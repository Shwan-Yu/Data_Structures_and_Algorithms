class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        choices, res = list(range(1,n+1)), ""
        k -= 1 # index starts at 0: first element is the 0th element
        while n > 0: # when n = 1 we are actually manipulating 0th
            n -= 1
            index, k = divmod(k, math.factorial(n)) 
            res += str(choices[index])
            del choices[index]
        return res
