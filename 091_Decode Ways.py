class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0": return 0
        dp = [1] + [0] * len(s)
        for i in range(1, len(s)+1):
            if s[i-1] != "0": dp[i] += dp[i-1]
            if i > 1 and "10"<=s[i-2:i]<="26": dp[i] += dp[i-2]
        return dp[len(s)]
    
# O(1) space
# class Solution(object):
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s or s[0] == "0": return 0
#         dp1, dp2 = 0, 1
#         for i in range(1, len(s)+1):
#             tmp = 0
#             if s[i-1] != "0": tmp += dp2
#             if i > 1 and "10"<=s[i-2:i]<="26": tmp+=dp1
#             dp1 = dp2; dp2 = tmp
#         return dp2
