class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(n)
        if not nums or len(nums) < k: return []
        dp = [0]*len(nums)
        dp[0] = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            dp[i] = dp[i-1]+nums[i+k-1]-nums[i-1]
        # if i current val is bigger than i+1 max val(the maximum after i+1), we store the val and ind, else we put i+1 val and ind here
        max_last_one = [[0,0] for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            if dp[i] > max_last_one[i+1][0]:
                max_last_one[i] = dp[i], i
            else:
                max_last_one[i] = max_last_one[i+1]
        # if i current val+ max after i+k is bigger than i+1 max two sum val(the maximum sum after i+1), we store the val and two ind, else we put i+1 val and two ind here
        max_last_two = [[0,0,0] for i in range(len(nums))]
        for i in range(len(nums)-k-2,-1,-1):
            if dp[i]+max_last_one[i+k][0] > max_last_two[i+1][0]:
                max_last_two[i] = dp[i]+max_last_one[i+k][0], i, max_last_one[i+k][1]
            else:
                max_last_two[i] = max_last_two[i+1]
                
        max_sum, inds = 0, []       
        for i in range(len(nums)-3*k+1):
            sum_jl, ji, li = max_last_two[i+k]
            if dp[i]+sum_jl > max_sum:
                inds = [i, ji, li]
                max_sum = dp[i]+sum_jl
        return inds
        
#         O(n^2)
#         if not nums or len(nums) < k: return []
#         dp = [0]*len(nums)
#         dp[0] = sum(nums[:k])
#         for i in range(1, len(nums)-k+1):
#             dp[i] = dp[i-1]+nums[i+k-1]-nums[i-1]

#         MAX=[[0,0] for i in range(len(nums))]
#         for i in range(len(nums)-2,-1,-1):
#             MAX[i][0]=dp[i]
#             if MAX[i+1][0]>MAX[i][0]:
#                 MAX[i]=MAX[i+1]
#             else:
#                 MAX[i][1]=i
        
#         # intervals should be k-1
#         max_sum, inds = 0, []
#         for i in range(len(nums)-3*k+1):
#             for j in range(i+k, len(nums)-2*k+1):
#                 l, li = MAX[j+k]
#                 if dp[i]+dp[j]+l > max_sum:
#                     inds = [i, j, li]
#                     max_sum = dp[i]+dp[j]+l
#         return inds
        
        # O(n^3)
        # if not nums or len(nums) < k: return []
        # dp = [0]*len(nums)
        # dp[0] = sum(nums[:k])
        # for i in range(1, len(nums)-k+1):
        #     dp[i] = dp[i-1]+nums[i+k-1]-nums[i-1]
        # # intervals should be k-1
        # max_sum, inds = 0, []
        # for i in range(len(nums)-3*k+1):
        #     for j in range(i+k, len(nums)-2*k+1):
        #         for l in range(j+k, len(nums)-k+1):
        #             if dp[i]+dp[j]+dp[l] > max_sum:
        #                 inds = [i, j, l]
        #                 max_sum = dp[i]+dp[j]+dp[l]
        # return inds
