# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        def dfs(node, parent_val):
            if not node:
                return True
            l = dfs(node.left, node.val)
            r = dfs(node.right, node.val)
            if l and r:
                self.count += 1
            return l and r and node.val == parent_val
        
        dfs(root, None)
        return self.count
