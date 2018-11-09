"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        zero_th = Node(0, None, None)
        prev = zero_th
        stack, node = [], root
        
        while node:
                stack.append(node)
                node = node.left
        while stack:
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        zero_th.right.left, prev.right = prev, zero_th.right
        return zero_th.right
