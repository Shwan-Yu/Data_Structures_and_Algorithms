# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_sym(p, q):
            if p and q:
                return p.val == q.val and check_sym(p.left, q.right) and check_sym(p.right, q.left)
            return p is q
        
        if not root:
            return True
        return check_sym(root.left, root.right)
        
