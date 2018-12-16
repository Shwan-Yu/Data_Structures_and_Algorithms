class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n, row_lst, col_lst = len(grid), len(grid[0]), [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_lst.append(i); col_lst.append(j)
        col_lst.sort() # don't need to sort row_lst.
        mid_row, mid_col = row_lst[len(row_lst)//2], col_lst[len(col_lst)//2]
        return sum([abs(num-mid_row) for num in row_lst]) + sum([abs(num-mid_col) for num in col_lst])
