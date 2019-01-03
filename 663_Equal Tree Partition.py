# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # One pass
        self.sums = set()
        def allSum(node):
            if not node: return 0
            cur_sum = node.val + allSum(node.left) + allSum(node.right)
            if node is not root:
                self.sums.add(cur_sum)
            return cur_sum
            
        return allSum(root) % 2 == 0 and (allSum(root) // 2) in self.sums
