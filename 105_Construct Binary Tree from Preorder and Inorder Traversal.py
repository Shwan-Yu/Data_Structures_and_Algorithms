# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        
        root.left = self.buildTree(preorder[1:inorder_index + 1], inorder[:inorder_index])
        root.right = self.buildTree(preorder[inorder_index + 1:], inorder[inorder_index + 1:])
        return root
