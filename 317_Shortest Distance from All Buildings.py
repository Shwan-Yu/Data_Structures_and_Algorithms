class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, total_b = len(grid), len(grid[0]), 0
        dist = [[0]*n for i in range(m)]
        arrive_b = [[0]*n for i in range(m)]
        
        def bfs(grid, dist, arrive_b, i, j):
            q, memo,count = [(i,j)], set([(i,j)]), 0
            while q:
                newq = []
                for x, y in q:
                    for dx, dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                        if 0<=dx<m and 0<=dy<n and grid[dx][dy] == 0 and (dx, dy) not in memo:
                            newq.append((dx,dy))
                            memo.add((dx,dy))
                            dist[dx][dy] += count+1
                            arrive_b[dx][dy] += 1
                q, count = newq, count+1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total_b += 1
                    bfs(grid, dist, arrive_b, i, j)
        possi_dist = [dist[i][j] for i in range(m) for j in range(n) if grid[i][j] == 0 and arrive_b[i][j] == total_b]
        return min(possi_dist) if possi_dist else -1
