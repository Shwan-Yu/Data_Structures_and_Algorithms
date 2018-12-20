# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        nodeA, nodeB = headA, headB
        while nodeA is not nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
    
        # memo = set()
        # while headA:
        #     memo.add(headA)
        #     headA = headA.next
        # while headB:
        #     if headB in memo: return headB
        #     headB = headB.next
        # return None
