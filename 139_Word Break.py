class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i+1-len(word):i+1] and (dp[i-len(word)] or i-len(word) == -1):
                    dp[i] = True
        return dp[-1]
