# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("-inf") 
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.res = max(self.res, l + r + node.val)
            cur_best = max(l, r) + node.val
            return cur_best if cur_best > 0 else 0
        
        dfs(root)
        return self.res
