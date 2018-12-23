from collections import deque
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if forest[0][0] == 0: return -1
        m, n, count, start_p = len(forest), len(forest[0]), 0, (0,0)
        
        def findNextPos(forest, dq, memo, dest):
            for _ in range(len(dq)):
                i,j = dq.popleft()
                if (i,j) == dest: return True
                for d in ((1,0),(-1,0),(0,1),(0,-1)):
                    di,dj = i+d[0],j+d[1]
                    if 0<=di<m and 0<=dj<n and forest[di][dj] != 0 and (di, dj) not in memo:
                        dq.append((di,dj))
                        memo.add((di,dj))
            return False
    
        def cal_steps_bfs(forest, start, dest):
            dq = deque()
            dq.append(start)
            steps = 0
            memo = set([start])
            while dq:
                found = findNextPos(forest, dq, memo, dest)
                if found: break
                else: steps += 1
            return steps if found else -1
    
        heap = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        heapq.heapify(heap)
        while heap:
            next_h, next_i, next_j = heapq.heappop(heap)
            dis = cal_steps_bfs(forest, start_p, (next_i, next_j))
            if dis == -1: return -1
            count += dis
            start_p = (next_i, next_j)
        return count
