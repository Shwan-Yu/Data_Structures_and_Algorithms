class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        sum_k = sum(nums)
        if sum_k%k != 0: return False
        target = sum_k/k
        n = len(nums)
        memo = [0] * n
        
        def dfs(k, index, cur_sum):
            if k == 1: return True
            if cur_sum == target: return dfs(k-1,0,0)
            for i in range(index, n):
                if not memo[i] and cur_sum+nums[i]<=target:
                    memo[i] = 1
                    if dfs(k, i+1, cur_sum+nums[i]): return True
                    memo[i] = 0
            return False
        
        return dfs(k, 0, 0)
