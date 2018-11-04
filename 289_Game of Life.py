class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def liveNeighbors(board, i, j):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for d in directions:
                ni, nj = d[0]+i, d[1]+j
                if 0 <= ni <= len(board)-1 and 0 <= nj <= len(board[0])-1:
                    count += (board[ni][nj] & 1)
            return count
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = liveNeighbors(board, i, j)
                if board[i][j] == 1 and (n == 2 or n == 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and n == 3:
                    board[i][j] = 2
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
