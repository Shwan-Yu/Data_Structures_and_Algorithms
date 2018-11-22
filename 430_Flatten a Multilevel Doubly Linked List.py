"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        dummy = prev = Node(0, None, head, None)
        stack = [head]
        while stack:
            node = stack.pop()
            prev.next, node.prev = node, prev
            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            prev = node
        dummy.next.prev = None
        return dummy.next
