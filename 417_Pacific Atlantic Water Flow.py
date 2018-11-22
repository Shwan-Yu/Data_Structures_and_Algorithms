class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        p_memo = [[False for j in range(n)] for i in range(m)]
        a_memo = [[False for j in range(n)] for i in range(m)]
        
        def dfs(i,j,memo):
            if memo[i][j]: return
            memo[i][j] = True
            for d in ((-1,0),(0,-1),(1,0),(0,1)):
                di, dj = i+d[0], j+d[1]
                if 0<=di<m and 0<=dj<n and matrix[di][dj] >= matrix[i][j]: dfs(di,dj,memo)
        
        for i in range(m):
            dfs(i,0,p_memo)
            dfs(i,n-1,a_memo)
        for j in range(n):
            dfs(0,j,p_memo)
            dfs(m-1,j,a_memo)
            
        res = []
        for i in range(m):
            for j in range(n):
                if p_memo[i][j] and a_memo[i][j]:
                    res.append([i,j])
        return res
