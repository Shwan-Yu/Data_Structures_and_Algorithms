# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(node, l_boundary, r_boundary):
            if not node:
                return True
            if not l_boundary < node.val < r_boundary:
                return False
            return isValid(node.left, l_boundary, node.val) and isValid(node.right, node.val, r_boundary)
        
        return isValid(root, float("-inf"), float("inf"))
