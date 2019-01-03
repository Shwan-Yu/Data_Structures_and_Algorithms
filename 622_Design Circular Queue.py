class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.lst = [0] * k
        self.size, self.k = 0, k
        self.l = self.r = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.lst[self.r] = value
            self.r = (self.r+1) % self.k
            self.size += 1
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.l = (self.l+1) % self.k
            self.size -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.lst[self.l] if self.size else -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        # for this part, because it's python so 0-1 = -1 is also a valid indexing, so just "self.r-1" may also work, but I just want to be clearer. 
        return self.lst[(self.r+self.k-1)%self.k] if self.size else -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return True if not self.size else False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return True if self.size == self.k else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
