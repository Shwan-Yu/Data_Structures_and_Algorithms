class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix sum
        # []
        # [ ]
        # [  ]
        # ......
        # [                ]
        # record every []'s ending index, only the first ending, because we want longest middle.
        # when one [] includes k in it, suppose:
        # [  ][ this is k  ] = cum_sum
        # so cum_sum-k should be already in our record
        # we have:
        #    e             i
        # [  ][ this is k  ]
        # so length e to i is i-e
        
        res = cum_sum = 0
        prefix = {0:-1}
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum not in prefix:
                prefix[cum_sum] = i
            if cum_sum-k in prefix:
                res = max(res, i - prefix[cum_sum-k])
        return res
