class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # a % k, (a%k + b) % k, need prove, next time
        if k == 0: return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
        mod, mod_sum = {0:-1}, 0
        for i, num in enumerate(nums):
            mod_sum = (mod_sum+num)%k
            if mod_sum in mod and i - mod[mod_sum] >= 2: return True
            if mod_sum not in mod: mod[mod_sum] = i
        return False
