# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left) 
            r = dfs(node.right)
            
            l = l + 1 if node.left and node.val == node.left.val else 0
            r = r + 1 if node.right and node.val == node.right.val else 0
            
            self.res = max(self.res, l + r)
            cur = max(l, r)
            return cur 
        
        self.res = 0
        dfs(root)
        return self.res
