class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        memo = [0] * len(graph)
        
        def checkNei(i, color):
            memo[i] = color
            for nei in graph[i]:
                if memo[nei] == memo[i]: return False
                if not memo[nei] and not checkNei(nei, -color): return False
            return True
            
        for i in range(len(graph)):
            if not memo[i]:
                if not checkNei(i, 1): return False
        return True
