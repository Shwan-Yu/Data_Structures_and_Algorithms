class Solution:
    def exist(self, board, word):
        if not board:
            return False
        
        m,n = len(board), len(board[0])
        
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = "#"
            res = dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:]) or dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:])
            board[i][j] = tmp
            return res
            
        
        for i in range(m):
            for j in range(n):
                if dfs(board, i, j, word):
                    return True
        return False

  
    
