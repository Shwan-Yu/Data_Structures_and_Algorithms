# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # reverse the linked lists and add them, them reverse back
        
        # not reverse the linked lists.
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry, next_node = 0, None
        while stack1 or stack2 or carry:
            v1 = v2 = 0
            if stack1: v1 = stack1.pop()
            if stack2: v2 = stack2.pop()
            carry, value = divmod(v1+v2+carry, 10)
            node = ListNode(value)
            node.next = next_node
            next_node = node
        return node
        
        # cast them into str and add them
        # s1, s2 = "", ""
        # while l1:
        #     s1 += str(l1.val)
        #     l1 = l1.next
        # while l2:
        #     s2 += str(l2.val)
        #     l2 = l2.next
        # num1, num2 = int(s1), int(s2)
        # res = str(num1+num2)
        # head = node = ListNode(int(res[0]))
        # for i in range(1, len(res)):
        #     node.next = ListNode(int(res[i]))
        #     node = node.next
        # return head
