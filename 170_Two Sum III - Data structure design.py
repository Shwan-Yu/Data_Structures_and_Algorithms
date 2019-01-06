class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pool = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.pool[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.pool:
            if value - num in self.pool and (value - num != num or self.pool[num] > 1): return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
