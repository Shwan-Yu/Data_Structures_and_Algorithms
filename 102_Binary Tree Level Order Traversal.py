# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = [root]
        res = []
        
        while level:
            res.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            
        return res
