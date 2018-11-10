# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def checkEqual(s, t):
            if s and t:
                return s.val == t.val and checkEqual(s.left, t.left) and checkEqual(s.right, t.right)
            return s is t
        
        if not s:
            return False
        return checkEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
