class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def rec_cs(nums, target, index, path, res):
            if target == 0:
                res.append(path)
            else:
                for i in range(index, len(nums)):
                    if target < nums[i]:
                        break
                    if i != index and nums[i] == nums[i - 1]:
                        continue
                    rec_cs(nums, target - nums[i], i + 1, path + [nums[i]], res)
                    
        res = []
        candidates.sort()
        rec_cs(candidates, target, 0, [], res)
        return res
