# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # This is for BT
#         if not root:
#             return None
#         if root == p or root == q:
#             return root
#         l = r = None
#         l = self.lowestCommonAncestor(root.left, p, q)
#         r = self.lowestCommonAncestor(root.right, p, q)
        
#         if l and r:
#             return root
#         else:
#             return l or r
