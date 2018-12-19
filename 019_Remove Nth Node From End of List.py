# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # not in one pass, reverse the linked list and get nth
        
        # in case we need to remove the first
        prev = node = dummy = ListNode(0)
        node.next = head
        for i in range(n):
            node = node.next
        while node.next:
            prev, node = prev.next, node.next
        prev.next = prev.next.next
        return dummy.next
