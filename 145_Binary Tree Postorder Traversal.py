# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # right preorder and reverse
        stack, res, node = [], [], root
        while node:
            stack.append(node)
            res.append(node.val)
            node = node.right
        while stack:
            node = stack.pop()
            node = node.left
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.right
        return res[::-1]
        
#         self.res = []
#         def traversal(node):
#             if not node: return
#             traversal(node.left)
#             traversal(node.right)
#             self.res.append(node.val)
            
#         traversal(root)
#         return self.res
