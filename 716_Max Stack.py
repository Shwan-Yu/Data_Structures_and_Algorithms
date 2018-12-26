class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append((x, max(x, self.stack[-1][1]) if self.stack else x))

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        # O(n) worst case
        record = []
        val = self.stack[-1][1]
        i = len(self.stack)-1
        while self.stack:
            cur = self.stack.pop()[0]
            if cur == val:
                break
            record.append(cur)
        for x in record[::-1]: self.push(x)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
