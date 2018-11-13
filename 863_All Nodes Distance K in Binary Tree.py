# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        import collections
        nei = collections.defaultdict(list)
        def link(par, kid):
            if par and kid:
                nei[par.val].append(kid.val)
                nei[kid.val].append(par.val)
            if kid.left: link(kid, kid.left)
            if kid.right: link(kid, kid.right)
            
        link(None, root)
        res = [target.val]
        memo = set(res)
        for i in range(K):
            res = [neighbor for start in res for neighbor in nei[start] if neighbor not in memo]
            memo = memo.union(res)
        return res
