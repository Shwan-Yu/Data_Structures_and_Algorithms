# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # O(n)
        memo = set()
        while head:
            if head in memo: return head
            memo.add(head)
            head = head.next
        return None
