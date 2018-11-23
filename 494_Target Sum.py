class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        for new_val in nums:
            cur_sum = collections.defaultdict(int)
            for pre_sum in prefix_sum:
                cur_sum[pre_sum+new_val] += prefix_sum[pre_sum]
                cur_sum[pre_sum-new_val] += prefix_sum[pre_sum]
            prefix_sum = cur_sum
        return prefix_sum[S]
