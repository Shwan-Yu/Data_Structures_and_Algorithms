class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.lst = []
        self.size = size
        self.l = 0
        self.sum_w = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # use a lot of memory, we can also pop it out then we don't need self.l
        if len(self.lst) >= self.size:
            self.sum_w -= self.lst[self.l]
            self.l += 1
        self.lst.append(val)
        self.sum_w += val
        return float(self.sum_w)/(len(self.lst)-self.l)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
