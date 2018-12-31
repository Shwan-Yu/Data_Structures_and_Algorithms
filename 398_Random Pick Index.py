class Solution(object):
    import random
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.m = collections.defaultdict(list)
        for i, val in enumerate(nums):
            self.m[val].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice(self.m[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
