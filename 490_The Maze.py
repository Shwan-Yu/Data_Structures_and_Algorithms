class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
#         BFS
        m, n, q, stopped = len(maze), len(maze[0]), [(start[0], start[1])], {(start[0], start[1])}
        while q:
            i, j = q.pop(0)
            if [i, j] == destination:
                return True
            for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                di, dj = i, j
                while 0 <= di+d[0] < m and 0 <= dj+d[1] < n and maze[di+d[0]][dj+d[1]] == 0:
                    di += d[0]
                    dj += d[1]
                if (di, dj) not in stopped:
                    stopped.add((di,dj))
                    q.append((di,dj))
        return False
        
#         DFS
#         m, n = len(maze), len(maze[0])
#         def reachDes(i, j, stop_points):
#             if (i,j) in stop_points: return False
#             stop_points.add((i,j))
#             if [i,j] == destination: return True
#             nei = [(0,1),(0,-1),(1,0),(-1,0)]
#             for d in nei:
#                 di, dj = i, j
#                 while 0<=di+d[0]<m and 0<=dj+d[1]<n and maze[di+d[0]][dj+d[1]] == 0:
#                     di, dj = di+d[0], dj+d[1]
#                 if reachDes(di, dj, stop_points): return True
#             return False
        
#         stop_points = set()
#         return reachDes(start[0], start[1], stop_points)
