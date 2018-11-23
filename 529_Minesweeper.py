class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board: return None
        ci, cj = click[0], click[1]
        if board[ci][cj] == "M":
            board[ci][cj] = "X"
            return board
        
        m, n = len(board), len(board[0])
        def countMine(i, j):
            board[i][j] = "#"
            count = 0
            nei = [(0,1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,1),(1,0),(1,-1)]
            for d in nei:
                di, dj = i+d[0], j+d[1]
                if 0<=di<m and 0<=dj<n and board[di][dj] == "M":
                    count += 1
            if count:
                board[i][j] = str(count)
                return
            board[i][j] = "B"
            for d in nei:
                di, dj = i+d[0], j+d[1]
                if 0<=di<m and 0<=dj<n and board[di][dj] == "E":
                    countMine(di, dj)
        countMine(ci, cj)
        return board
