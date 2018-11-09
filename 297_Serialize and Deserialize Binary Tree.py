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
        if not root: return "None,"
        return "{},".format(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(data):
            if self.count >= len(data) or data[self.count] == "None":
                self.count += 1
                return None
            node = TreeNode(int(data[self.count]))
            self.count += 1
            node.left = build_tree(data)
            node.right = build_tree(data)
            return node
            
        if not data:
            return
        data = data[:-1].split(",")
        self.count = 0
        return build_tree(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
