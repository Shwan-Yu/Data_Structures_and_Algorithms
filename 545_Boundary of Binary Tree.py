# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def left_bound(node):
            if not node or (not node.left and not node.right): return
            self.res.append(node.val)
            if node.left: 
                left_bound(node.left)
            else: 
                left_bound(node.right)
            
        def leaves(node):
            if not node: return
            leaves(node.left)
            if node != root and (not node.left and not node.right):
                self.res.append(node.val)
            leaves(node.right)
            
        def right_bound(node):
            if not node or (not node.left and not node.right): return
            if node.right: 
                right_bound(node.right)
            else: 
                right_bound(node.left)
            self.res.append(node.val)
            
        if not root: return []
        self.res = [root.val]
        left_bound(root.left)
        leaves(root)
        right_bound(root.right)
        return self.res
