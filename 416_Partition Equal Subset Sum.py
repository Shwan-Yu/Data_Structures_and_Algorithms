class Solution(object):
    def canPartition(self, nums):
        memo = set()
        def helper(start, target):         # Here path is not needed
            if (start, target) in memo:
                return False
            if target < 0:
                return
            elif target == 0:
                return True
            for i in xrange(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            memo.add((start, target))
            return False
        return False if sum(nums)%2 else helper(0, sum(nums)/2)
