# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            self.res.append(node.val)
            dfs(node.right)
            
        dfs(root)
        return self.res
