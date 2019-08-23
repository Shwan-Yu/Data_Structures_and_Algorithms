class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap(object):

    def __init__(self, capacity = 500):
        """
        Initialize your data structure here.
        """
        self.capacity = capacity
        self.lst = [None] * capacity

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        ind = hash(key) % self.capacity
        head = self.lst[ind]
        while head:
            if head.key == key: 
                head.val = value
                return
            head = head.next
        newNode = Node(key, value)
        newNode.next = self.lst[ind]
        self.lst[ind] = newNode
            

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        ind = hash(key) % self.capacity
        head = self.lst[ind]
        while head:
            if head.key == key: 
                # print(head.next)
                return head.val
            head = head.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        ind = hash(key) % self.capacity
        head = self.lst[ind]
        if not head: return -1
        if head and head.key == key:
            self.lst[ind] = head.next
            return
        prev = head
        head = head.next
        while head:
            if head.key == key: 
                prev.next = head.next
                return
            head = head.next
            prev = prev.next
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
