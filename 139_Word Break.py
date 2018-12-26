class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # condition: prev True and cur == word
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
        return dp[-1]
