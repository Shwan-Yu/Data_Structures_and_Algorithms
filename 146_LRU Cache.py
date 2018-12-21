class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.l = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic: return -1
        node = self.dic[key]
        val = node.val
        self._remove(node)
        self._add(node)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # define used: put same key is also defined as used
        if key in self.dic: self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.l:
            node_rem = self.head.next
            self._remove(node_rem)
            del self.dic[node_rem.key]
    
    def _add(self, node):
        pre = self.tail.prev
        pre.next = node
        self.tail.prev = node
        node.prev = pre
        node.next = self.tail
        
    def _remove(self, node):
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
