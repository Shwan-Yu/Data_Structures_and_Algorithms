class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = res = 0
        while i < len(nums):
            cur = 1
            while i+1 < len(nums) and nums[i]<nums[i+1]:
                cur, i = cur+1, i+1
            res = max(res, cur)
            i+=1
        return res
    
        # sliding window, slow
        # l = i = 0
        # while i < len(nums):
        #     if any(nums[j] - nums[j-1] <= 0 for j in range(l+1,i+1)):
        #         l+=1
        #     i+=1
        # return i-l
