# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre or not post:
            return None
        root = TreeNode(pre[0])
        pre, post = pre[1:], post[:-1]
        if not pre or not post:
            return root
        left_root = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:left_root+1], post[:left_root+1])
        root.right = self.constructFromPrePost(pre[left_root+1:], post[left_root+1:])
        return root
        
