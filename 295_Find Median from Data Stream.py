class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max in the smallest and min in the largest
        self.sma, self.lar = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.sma) == len(self.lar):
            heapq.heappush(self.lar, -heapq.heappushpop(self.sma, -num))
        else:
            heapq.heappush(self.sma, -heapq.heappushpop(self.lar, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.sma) == len(self.lar):
            return float((self.lar[0] - self.sma[0])) / 2
        else:
            return float(self.lar[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
