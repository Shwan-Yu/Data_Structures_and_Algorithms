# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        while l1 or l2:
            v1 = v2 = float("inf")
            if l1: v1 = l1.val
            if l2: v2 = l2.val
            if v1 > v2:
                node.next = ListNode(v2)
                l2 = l2.next
            else:
                node.next = ListNode(v1)
                l1 = l1.next
            node = node.next
        return dummy.next
