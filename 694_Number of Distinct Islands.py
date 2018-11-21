class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        res = set()
        m, n = len(grid), len(grid[0])
        def recordIsland(i, j, patterns, cur_pos):
            grid[i][j] = 0
            nei = [(1,0), (-1,0), (0,1), (0,-1)]
            for d in nei:
                di, dj = i+d[0], j+d[1]
                if 0<=di<m and 0<=dj<n and grid[di][dj] == 1:
                    next_pos = (cur_pos[0]+d[0], cur_pos[1]+d[1])
                    patterns.append(next_pos)
                    recordIsland(di, dj, patterns, next_pos)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    patterns = []
                    recordIsland(i, j, patterns, (0,0))
                    res.add((tuple(patterns)))
        return len(res)
