class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1+dfs(i, j-1)+dfs(i,j+1)+dfs(i-1,j)+dfs(i+1,j)
            return area
        
        areas = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    areas.append(dfs(i,j))
                    
        return max(areas) if areas else 0
