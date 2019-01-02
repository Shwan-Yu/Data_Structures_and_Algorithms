class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtracking(nums, index, path, res):
            if len(path) >= 2:
                res.add(tuple(path))
            for i in range(index, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtracking(nums, i+1, path+[nums[i]], res)
        
        res = set()
        backtracking(nums, 0, [], res)
        return map(tuple, res)
