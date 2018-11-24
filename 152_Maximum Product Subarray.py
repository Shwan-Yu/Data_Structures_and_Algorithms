class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        max_res = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            cur_max, cur_min = max(nums[i], nums[i]*cur_max, nums[i]*cur_min), min(nums[i], nums[i]*cur_max, nums[i]*cur_min)
            max_res = max(max_res, cur_max)
        return max_res
