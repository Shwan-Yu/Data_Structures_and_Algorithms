class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # O(mn(m+n)) time, O(1) space
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0: matrix[k][j] = "#"
                    for k in range(n):
                        if matrix[i][k] != 0:matrix[i][k] = "#"
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "#": matrix[i][j] = 0
        
        # O(mn) time, (m+n) space
        # row, col = set(), set()
        # m, n = len(matrix), len(matrix[0])
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0: 
        #             row.add(i)
        #             col.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in row or j in col: matrix[i][j] = 0
        
