class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # sliding window O(n)
        l = n_sum = 0
        res = float("inf")
        for r in range(len(nums)):
            n_sum += nums[r]
            # while condition: 1. update the res 2. update the condition 3. move left
            while n_sum >= s:
                res = min(res, r - l+1)
                n_sum -= nums[l]
                l += 1
        # if there isn't one
        return res if res != float("inf") else 0
