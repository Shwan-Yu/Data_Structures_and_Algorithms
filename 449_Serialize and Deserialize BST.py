# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        return "{} ".format(root.val) + self.serialize(root.left) + self.serialize(root.right)
#         stack, res =[], []
#         node = root
#         while node:
#             res.append(str(node.val))
#             stack.append(node)
#             node = node.left
#         while stack:
#             node = stack.pop()
#             node = node.right
#             while node:
#                 res.append(str(node.val))
#                 stack.append(node)
#                 node = node.left
                
#         return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        stack = []
        data = [int(d) for d in data[:-1].split(" ")]
        root = node = TreeNode(data[0])
        for val in data[1:]:
            if val < node.val:
                node.left = TreeNode(val)
                stack.append(node)
                node = node.left
            else:
                while stack and stack[-1].val < val:
                    node = stack.pop()
                node.right = TreeNode(val)
                node = node.right
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
