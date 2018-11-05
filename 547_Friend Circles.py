class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        def dfs(M, node):
            visited.add(node)
            for fri_id in range(len(M)):
                if M[node][fri_id] != 1 or fri_id in visited:
                    continue
                dfs(M, fri_id)
            
        visited = set()
        count = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(M, i)
                count += 1
