# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse_n_ele(head, n):
            cur, prev = head, None
            while n > 0:
                head = head.next
                cur.next = prev
                prev = cur
                cur = head
                n -= 1
            return (prev, cur) # 1,2,3,4. None<-1<-2<-3  4, return 3, 4
        
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        prev_list, new_start = reverse_n_ele(head, count)
        # whole function reverse the first group
        head.next = self.reverseKGroup(new_start, k)
        return prev_list
