# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            prev = None
            node = cur = head
            while node:
                node = node.next
                cur.next = prev
                prev = cur
                cur = node
            return prev
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        odd = True if fast else False
        if odd: slow = slow.next
        another_head = reverse(slow)
        while head and another_head:
            if head.val != another_head.val: return False
            head, another_head = head.next, another_head.next
        return True
