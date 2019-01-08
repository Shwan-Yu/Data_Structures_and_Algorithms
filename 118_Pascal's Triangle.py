class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 1
        # 1 1
        # 1 1 1
        # 1 1 1 1
        # 1 1 1 1 1
        # j upper bound is i
        if not numRows: return []
        triangle = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j]
        return triangle
