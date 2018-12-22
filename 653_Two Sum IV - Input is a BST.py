# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        memo, stack = set(), []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            if k-node.val in memo:
                return True
            memo.add(node.val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return False
