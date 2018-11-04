class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def NSum(nums, target, N, rec_result, final_result):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    t_sum = nums[l] + nums[r]
                    if t_sum < target:
                        l += 1
                    elif t_sum > target:
                        r -= 1
                    else:
                        final_result.append(rec_result + [nums[l], nums[r]])
                        while l < r and nums[l + 1] == nums[l]:
                            l += 1
                        while l < r and nums[r - 1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i > 0 and nums[i] == nums[i - 1]:
                        continue
                    NSum(nums[i + 1:], target - nums[i], N - 1, rec_result + [nums[i]], result)
        
        result = []
        NSum(sorted(nums), target, 4, [], result)
        return result
        
