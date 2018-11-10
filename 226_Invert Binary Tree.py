# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def invert(node):
            if not node:
                return None
            l = invert(node.left)
            r = invert(node.right)
            node.left = r
            node.right = l
            return node
        return invert(root)
