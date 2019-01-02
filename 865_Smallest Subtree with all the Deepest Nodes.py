# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dic = {root: None}
        q = [root]
        # First BFS, for every node in this level, record its two children and link its children back with itself
        while q:
            newq = []
            for parent in q:
                for child in (parent.left, parent.right):
                    if child:
                        dic[child] = parent
                        newq.append(child)
            # if not newq, means that we reach all the deepest nodes, all deepest nodes are stored in q, we break it out and use q to do the next step.
            if not newq:
                break
            q = newq
        
        # Second BFS, bottom up, when we have just one parent, we find the answer.
        par = set(q)
        while len(par) != 1:
            new_par = set(dic[node] for node in par)
            par = new_par
        return par.pop()
