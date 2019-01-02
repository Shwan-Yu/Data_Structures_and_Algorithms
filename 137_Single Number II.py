class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for num in nums:
            a = a ^ num & ~b
            b = b ^ num & ~a
        return a
        
        # extra memory
        # count = collections.Counter(nums)
        # for k, v in count.items():
        #     if v == 1: return k
        # return
