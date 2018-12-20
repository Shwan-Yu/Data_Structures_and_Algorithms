# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(start):
            new_head = start.next
            if new_head:
                next_head = new_head.next
                new_head.next = start
            return (new_head, next_head)
        
        if not head or not head.next: return head
        new_head, next_head = swap(head)
        head.next = self.swapPairs(next_head)
        return new_head
            
            
                
