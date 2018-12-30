# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        stack= []
        slow = node = head
        fast = slow.next
        # find the middle part
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # start from slow.next and cut down the first half
        new_slow = slow.next
        slow.next = None
        # append second half to the stack
        while new_slow:
            stack.append(new_slow)
            new_slow = new_slow.next
        # link first node with stack.pop() then link it to the second, if not stack, means we reach the last element. It was already linked to None before, so no need to take care of it.
        while node:
            next_n = node.next
            if stack:
                node.next = stack.pop()
                node.next.next = next_n
            node = next_n
