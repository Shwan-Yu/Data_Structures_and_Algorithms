class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [0] * (n+1)
        lst[0] = lst[1] = 1
        
        for total in range(2, n+1):
            for i in range(1, total+1):
                lst[total] += lst[i-1] * lst[total-i]
        return lst[n]
