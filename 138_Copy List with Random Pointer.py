# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        copy_dic = {}
        copy = link = head
        #copy process
        while copy:
            copy_dic[copy] = RandomListNode(copy.label)
            copy = copy.next
        while link:
            copy_dic[link].next = copy_dic.get(link.next)
            copy_dic[link].random = copy_dic.get(link.random)
            link = link.next
        return copy_dic.get(head)
