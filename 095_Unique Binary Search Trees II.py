# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        
        def build_tree(lst):
            if not lst:
                return [None]
            res = []
            for i in range(len(lst)):
                for left in build_tree(lst[:i]):
                    for right in build_tree(lst[i+1:]):
                        node = TreeNode(lst[i])
                        node.left, node.right = left, right
                        res.append(node)
            return res
            
        return build_tree([i for i in range(1, n+1)])
