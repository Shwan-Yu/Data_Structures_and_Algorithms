class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # e.g. 2 2 2 3
        # 0010 0010 0010 0011
        #   a      b
        # 0010    0000
        # 0000    0010
        # 0000    0000
        # a ^ num & 1111 -> ~b
        # a ^ num & xxxx -> ~b
        # a ^ num & ~(a^num) -> ~b
        
        # b ^ num & ~(b^num) -> ~a
        # ...
        
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
