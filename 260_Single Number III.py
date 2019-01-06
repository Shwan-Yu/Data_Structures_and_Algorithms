class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 0110
        # 1. find the index of digit that is a 1 in the xor of the two numbers, that means they are different at the position
        # 2. divide the whole nums into two groups, one with index 1 there and one with 0
        # 3. xor both groups, what are left are the two numbers
        
        xor = 0
        for num in nums:
            xor ^= num
        # now we got the xor of the two numbers
        
        # if not 1 in xor at this position, the "and" operation would give a 0
        find_one = 1
        while not xor & find_one:
            find_one <<= 1
        # now we found one digit that is 1
        
        # split them into two groups
        numi, numj = 0, 0
        for num in nums:
            if num & find_one:
                numi ^= num
            else:
                numj ^= num
        return [numi, numj]
