class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: return "1"
        if n == 2: return "11"
        def countSay(string):
            res, count = "", 1
            for i in range(1, len(string)):
                if string[i-1] == string[i]: count += 1
                else: 
                    res += str(count) + string[i-1] 
                    count = 1
                if i == len(string)-1: res += str(count) + string[i]
            return res
        
        dp = [""] * (n+1)
        dp[1], dp[2] = "1", "11"
        for i in range(3, n+1):
            count = 1
            dp[i] = countSay(dp[i-1])
        return dp[n]
