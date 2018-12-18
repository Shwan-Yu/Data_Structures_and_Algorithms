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
        res = []
        for node in lists:
            while node:
                res.append(node.val)
                node = node.next
        if not res: return
        res.sort()
        head = node = ListNode(res[0])
        for i in range(1,len(res)):
            node.next = ListNode(res[i])
            node = node.next
        return head
