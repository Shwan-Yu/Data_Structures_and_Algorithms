class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)]
        coord = [[(i,j) for j in range(n)] for i in range(n)]
        val = 1
        while val <= n*n:
            # remember to pop the first line
            for i, j in coord.pop(0):
                res[i][j] = val
                val+=1
            coord = zip(*coord)[::-1]
        return res
