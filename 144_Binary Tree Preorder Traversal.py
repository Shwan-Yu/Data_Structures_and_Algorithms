# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        stack, res = [], []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
            
        return res
    
        # res = []
        # def dfs(node):
        #     if not node: return
        #     res.append(node.val)
        #     dfs(node.left), dfs(node.right)
        # dfs(root)
        # return res
