# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # merge
        def merge(l, r):
            if not l or not r: return l or r
            if l.val > r.val: l, r = r, l
            head = prev = l
            l = l.next
            while l and r:
                if l.val < r.val: l = l.next
                else:
                    prev.next = r
                    r_next = r.next
                    r.next = l
                    r = r_next
                prev = prev.next
            prev.next = l or r
            return head
        # sort       
        if not head or not head.next: return head
        slow, fast = head, head.next # fast need to be next, 1->2 situation, stop move slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        another_head = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(another_head)
        return merge(l,r)
