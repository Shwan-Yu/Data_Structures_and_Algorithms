class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        from collections import deque
        self.q = deque([deque(i) for i in (v1, v2) if i])

    def next(self):
        """
        :rtype: int
        """
        deq = self.q.popleft()
        val = deq.popleft()
        if deq: self.q.append(deq)
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.q else False
        
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
