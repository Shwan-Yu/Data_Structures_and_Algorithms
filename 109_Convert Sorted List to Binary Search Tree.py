# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return
        if not head.next: return TreeNode(head.val)
        findMid, findLast = head, head.next.next
        while findLast and findLast.next:
            findMid = findMid.next
            findLast = findLast.next.next
        rootNode = findMid.next
        findMid.next = None
        root = TreeNode(rootNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rootNode.next)
        return root
        
