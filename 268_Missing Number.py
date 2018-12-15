class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)
        
        # Counter
        # count = collections.Counter(nums)
        # for i in xrange(len(nums)+1): count[i] -= 1
        # return count.most_common()[-1][0]
