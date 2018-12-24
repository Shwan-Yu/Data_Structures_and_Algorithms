# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_diff,last_node = float("inf"), None
        node, stack = root, []
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            if last_node:
                min_diff = min(min_diff, abs(node.val-last_node.val))
            last_node = node
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return min_diff
