# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def dfs(t1, t2):
            if not t1 or not t2:
                return t1 or t2
            
            t3 = TreeNode(t1.val + t2.val)
            t3.left = dfs(t1.left, t2.left)
            t3.right = dfs(t1.right, t2.right)
            return t3
        
        return dfs(t1, t2)
