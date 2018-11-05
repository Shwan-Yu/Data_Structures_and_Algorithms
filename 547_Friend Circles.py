class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        m = len(M)
        
        def dfs(M, node):
            visited.add(node)
            for friend_i in range(m):
                if friend_i in visited or M[node][friend_i] == 0:
                    continue
                dfs(M, friend_i)
            
        visited = set()
        count = 0
        for node in range(m):
            if node not in visited:
                dfs(M, node)
                count += 1
        return count
