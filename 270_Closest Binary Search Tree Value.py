# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff, res = float("inf"), 0
        node = root
        while node:
            new_diff = abs(node.val-target)
            if new_diff < diff:
                diff, res = new_diff, node.val
            node = node.left if node.val > target else node.right
        return res
        
