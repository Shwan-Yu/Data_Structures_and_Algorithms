class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def liveNeighbors(board, i, j):
            pos = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
            count = 0
            for p in pos:
                ni, nj = i + p[0], j + p[1]
                if 0 <= ni < m and 0 <= nj < n:
                    count += (board[ni][nj] & 1)
            return count
            
        for i in range(m):
            for j in range(n):
                count = liveNeighbors(board, i, j)
                if board[i][j] == 1 and (count == 2 or count == 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
