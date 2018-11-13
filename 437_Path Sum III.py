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
        :rtype: int
        """
        def dfs(node, target, cur_path, dic):
            if not node:
                return
            cur_path += node.val
            old_path = cur_path - target
            self.res += dic.get(old_path, 0)
            dic[cur_path] = dic.get(cur_path, 0) + 1
            dfs(node.left, target, cur_path, dic)
            dfs(node.right, target, cur_path, dic)
            dic[cur_path] -= 1
            
        self.res = 0
        dic = {0:1}
        dfs(root, sum, 0, dic)
        return self.res
        
        
        
#         def count_path(root, sum):
#             if not root: return 0
#             return int(sum == root.val) + count_path(root.left, sum - root.val) + count_path(root.right, sum - root.val)
            
#         if not root:
#             return 0
#         return count_path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum) 
