class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        # all the 0s can start simultaneously
        if not rooms: return
        m, n, q = len(rooms), len(rooms[0]), []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            newq = []
            for i,j in q:
                dist = rooms[i][j]+1
                for di, dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=di<m and 0<=dj<n and rooms[di][dj] == 2147483647:
                        rooms[di][dj] = dist
                        newq.append((di,dj))
            q = newq
        
#         if not rooms: return
#         m, n = len(rooms), len(rooms[0])
#         def bfs(rooms, i, j):
#             q, count, memo = [(i,j)], 0, set([(i,j)])
#             while q:
#                 newq = []
#                 for pi, pj in q:
#                     if rooms[pi][pj] not in (0, -1):
#                         rooms[pi][pj] = min(rooms[pi][pj], count)
#                     for di, dj in ((pi+1,pj),(pi-1,pj),(pi,pj+1),(pi,pj-1)):
#                         if 0<=di<m and 0<=dj<n and (di,dj) not in memo and rooms[di][dj] not in (0,-1):
#                             newq.append((di,dj))
#                             memo.add((di,dj))
#                 count, q = count+1, newq        
        
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     bfs(rooms,i,j)
