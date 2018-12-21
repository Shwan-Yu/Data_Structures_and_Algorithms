# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        tail, node = head, head.next
        while node:
            if node.val == tail.val: tail.next = node.next
            else: tail = tail.next
            node = node.next
        return head
