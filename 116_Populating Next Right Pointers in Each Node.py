# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        cur = root
        next_line = cur.left
        while next_line:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = next_line
                next_line = cur.left
        # Not Inplace
        # if not root:
        #     return
        # res = []
        # level = [root]
        # while level:
        #     if len(level) > 1: 
        #         prev = level[0]
        #         for node in level[1:]:
        #             prev.next = node
        #             prev = node
        #     level = [kid for node in level for kid in (node.left, node.right) if kid]
