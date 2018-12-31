"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new = Node(insertVal, None)
        if not head:
            new.next = new
            return new
        prev, node = head, head.next
        while True:
            # insert at the two boundaries
            if prev.val > node.val and (insertVal >= prev.val or insertVal <= node.val): break
            # insert in the middle
            elif prev.val <= insertVal <= node.val: break
            # all the node vals are the same, doesn't matter where to insert
            elif node == head: break
            node = node.next
            prev = prev.next
        prev.next = new
        new.next = node
        return head
