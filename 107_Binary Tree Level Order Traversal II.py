# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
            level = [child for node in level for child in (node.left, node.right) if child]
            
        return res[::-1]
