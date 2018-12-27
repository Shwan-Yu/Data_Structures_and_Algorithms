# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        record = collections.defaultdict(list)
        q, res, min_i, max_i = [(0, root)], [], float("inf"), float("-inf")
        # search level by level
        while q:
            newq = []
            for i, node in q:
                if node:
                    # get the possible min and max index
                    min_i = min(min_i,i); max_i = max(max_i,i)
                    record[i].append(node.val)
                    newq.append((i-1, node.left))
                    newq.append((i+1, node.right))
            q = newq
        # indexes are already in order, just get it out and return
        for i in range(min_i,max_i+1):
            res.append(record[i])
        return res
        
