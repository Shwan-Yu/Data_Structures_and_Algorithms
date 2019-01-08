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
        # meeting point k: 2K-K = nC
        # from circle start to meeting point: m: res_dis = K-m = nC-m = (n-1)C + (C-m)
        # make n = 1, from start to starting point = from meeting point to starting point
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        else: return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
        
        # O(n)
        # memo = set()
        # while head:
        #     if head in memo: return head
        #     memo.add(head)
        #     head = head.next
        # return None
        
