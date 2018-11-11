# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(node, sum):
            if not node:
                return False
            if not node.left and not node.right and node.val == sum:
                return True
            return dfs(node.left, sum - node.val) or dfs(node.right, sum - node.val)
            
        return dfs(root, sum)
