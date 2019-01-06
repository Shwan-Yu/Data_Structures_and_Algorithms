class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 2^n -1
        res = [[]]
        for num in nums:
            res += [ele + [num] for ele in res]
        return res
        
        # or
        # 2^n doubled at every time
#         def backtracking(nums, index, path, res):
#             res.append(path)
#             for i in range(index, len(nums)):
#                 backtracking(nums, i+1, path + [nums[i]], res)
               
#         res = []
#         backtracking(nums, 0, [], res)
#         return res
