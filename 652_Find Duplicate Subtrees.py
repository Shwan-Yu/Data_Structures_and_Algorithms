# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def dfs(node):
            if not node: return "N"
            subtree = dfs(node.left) + dfs(node.right) + str(node.val)
            if subtree in self.dic and self.dic[subtree] == 1:
                self.res.append(node)
            self.dic[subtree] = self.dic.get(subtree, 0) + 1
            return subtree
        
        self.res = []
        self.dic = {}
        dfs(root)
        return self.res
