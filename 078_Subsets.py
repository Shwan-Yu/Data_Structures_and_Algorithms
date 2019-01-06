class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [ele + [num] for ele in res]
        return res
        
        # or
        
#         def backtracking(nums, index, path, res):
#             res.append(path)
#             for i in range(index, len(nums)):
#                 backtracking(nums, i+1, path + [nums[i]], res)
               
#         res = []
#         backtracking(nums, 0, [], res)
#         return res
