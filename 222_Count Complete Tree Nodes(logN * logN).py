# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_dep(root):
            if not root:
                return 0
            return 1 + count_dep(root.left)
        
        if not root:
            return 0
        l_depth = count_dep(root.left)
        r_depth = count_dep(root.right)
        if l_depth == r_depth:
            return pow(2, l_depth) + self.countNodes(root.right)
        else:
            return pow(2, r_depth) + self.countNodes(root.left)
