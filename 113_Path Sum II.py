# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        def dfs(node, sum, path, res):
            if not node:
                return
            if not node.left and not node.right and node.val == sum:
                res.append(path + [node.val])
                return
            dfs(node.left, sum - node.val, path + [node.val], res)
            dfs(node.right, sum - node.val, path + [node.val], res)
            
        res = []   
        dfs(root, sum, [], res)
        return res
