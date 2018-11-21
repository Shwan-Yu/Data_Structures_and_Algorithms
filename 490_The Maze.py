class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        def reachDes(i, j, stop_points):
            if (i,j) in stop_points: return False
            stop_points.add((i,j))
            if [i,j] == destination: return True
            nei = [(0,1),(0,-1),(1,0),(-1,0)]
            for d in nei:
                di, dj = i, j
                while 0<=di+d[0]<m and 0<=dj+d[1]<n and maze[di+d[0]][dj+d[1]] == 0:
                    di, dj = di+d[0], dj+d[1]
                if reachDes(di, dj, stop_points): return True
            return False
        
        stop_points = set()
        return reachDes(start[0], start[1], stop_points)
