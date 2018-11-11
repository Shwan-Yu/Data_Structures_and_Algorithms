# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path, res):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path + str(root.val))
                return
            dfs(root.left, path + str(root.val) + "->", res)
            dfs(root.right, path + str(root.val) + "->", res)
            
        res = []
        dfs(root, "", res)
        return res
