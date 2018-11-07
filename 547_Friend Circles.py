class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        def dfs(M, i):
            visited.add(i)
            for j in range(len(M[i])):
                if M[i][j] == 1 and j not in visited:
                    dfs(M, j)
        
        visited = set()
        count = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(M, i)
                count += 1
        return count
