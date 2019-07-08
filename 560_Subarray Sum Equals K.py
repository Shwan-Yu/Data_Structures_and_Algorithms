class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1 1 1  k = 2
        # 1        []    cum_sum = 1 
        # 1 1      [k]   cum_sum = 2
        # 1 1 1    [][k]  cum_sum - k = 3 - 2 in the dictionary 
        
        # 1. update cum_sum
        # 2. check if cum_sum - k is in the dictionary, if in, add count
        # 3. update the dictionary
        
        dic, cum_sum, res = {0: 1}, 0, 0
        for num in nums:
            cum_sum += num
            res += dic.get(cum_sum-k, 0)
            dic[cum_sum] = dic.get(cum_sum, 0) + 1
        return res
