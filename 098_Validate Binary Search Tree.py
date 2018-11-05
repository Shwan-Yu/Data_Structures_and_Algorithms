# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def check_BST(node, left_sub, right_sub):
            if not node:
                return True
        
            if not left_sub < node.val < right_sub:
                return False
            
            return check_BST(node.left, left_sub, node.val) and check_BST(node.right, node.val, right_sub)
        
        return check_BST(root, float("-inf"), float("inf"))
