class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n, q, stop_point = len(maze), len(maze[0]), [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, i, j = heapq.heappop(q)
            if [i,j] == destination: return dist
            for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                di,dj,move = i,j,0
                while 0<=di+d[0]<m and 0<=dj+d[1]<n and maze[di+d[0]][dj+d[1]] == 0:
                    di+=d[0]
                    dj+=d[1]
                    move+=1
                if (di,dj) not in stop_point or dist+move<stop_point[(di,dj)]:
                    stop_point[(di,dj)] = dist+move
                    heapq.heappush(q,(dist+move, di, dj))
        return -1
