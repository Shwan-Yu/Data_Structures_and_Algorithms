# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop
        # O(nlog(n))
        # O(nlog(k))
        def gt(this, other):
            return this.val > other.val
        def lt(this, other):
            return this.val < other.val
        
        ListNode.__gt__ = gt
        ListNode.__lt__ = lt
        
        queue = []
        dummy = node = ListNode(0)
        for n in lists:
            if n: heappush(queue, n)
        while queue:
            cur = heappop(queue)
            node.next = cur
            if cur.next: 
                heappush(queue,cur.next)
            node = node.next
           
        return dummy.next
