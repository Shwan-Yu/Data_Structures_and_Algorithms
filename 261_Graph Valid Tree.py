class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1: return False
        node_map = collections.defaultdict(list)
        for i, j in edges:
            node_map[i].append(j)
            node_map[j].append(i)
        memo = set()
        
        def checkValid(i):
            if i in memo: return 
            memo.add(i)
            for nei in node_map[i]: checkValid(nei)
            
        checkValid(0)
        return len(memo) == n
