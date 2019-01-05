# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #     if 0 then move res:
    #     r   n
    #     1   2   3   4  (0,1): 

    #     r       n                     r   n
    #     1   2   3   4  (0,2) or   1   2   3   4  (0,2)

    #     stay at 1: 1/2 * 2/3 * 3/4 = 1/4
    #     stay at 2: 1/2 * 2/3 * 3/4 = 1/4
    
    # reservoir sampling solution
    def __init__(self, head):
        import random
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val
    
    
#     def __init__(self, head):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         :type head: ListNode
#         """
#         if using extra space, we can even store them into a list and do random
#         import random
#         self.l = 0
#         self.head = head
#         node = head
#         while node:
#             node = node.next
#             self.l += 1

#     def getRandom(self):
#         """
#         Returns a random node's value.
#         :rtype: int
#         """
#         seed = random.randint(0, self.l-1)
#         node = self.head
#         for i in range(seed):
#             node = node.next
#         return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
