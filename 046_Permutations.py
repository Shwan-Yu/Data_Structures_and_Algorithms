class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # O(n! factorial)
        def backtracking(nums, path, res):
            if len(nums)  == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                backtracking(nums[:i]+nums[i+1:], path+[nums[i]], res)
        res = []
        backtracking(nums, [], res)
        return res
