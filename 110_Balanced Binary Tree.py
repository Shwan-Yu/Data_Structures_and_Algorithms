# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        self.balance = True
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left) + 1
            r = dfs(node.right) + 1
            if abs(l-r) > 1: self.balance = False 
            return max(l, r)
        dfs(root)
        return self.balance
