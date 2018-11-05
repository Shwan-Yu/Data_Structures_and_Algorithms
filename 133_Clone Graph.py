# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited = {}
        def dfs(node):
            if not node or node in visited:
                return
            nodeCopy = UndirectedGraphNode(node.label)
            visited[nodeCopy.label] = nodeCopy
            nodeCopy.neighbors = [visited.get(nei.label) or dfs(nei) for nei in node.neighbors]
            return nodeCopy
            
        return dfs(node)
