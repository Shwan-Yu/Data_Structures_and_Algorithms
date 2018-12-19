# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        count, stack = 1, []
        dummy = prev = ListNode(0)
        prev.next = node = head
        while node and count < m:
            node = node.next
            prev = prev.next
            count += 1
        while node and count <= n:
            stack.append(node)
            node = node.next
            count += 1
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        prev.next = node
        return dummy.next
