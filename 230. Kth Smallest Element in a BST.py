# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.right)
            
        dfs(root)
        return self.res
        
        
        # stack = []
        # node = root
        # while node:
        #     stack.append(node)
        #     node = node.left
        # while stack:
        #     node = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return node.val
        #     node = node.right
        #     while node:
        #         stack.append(node)
        #         node = node.left
     
