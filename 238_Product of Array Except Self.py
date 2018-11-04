class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        
        tmp = 1
        for i in range(len(nums)):
            res[i] *= tmp
            tmp *= nums[i]
            
        tmp = 1
        for i in reversed(range(len(nums))):
            res[i] *= tmp
            tmp *= nums[i]
            
        return res
