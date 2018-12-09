class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r, memo = 0, 0, collections.defaultdict(int)
        while r < len(s):
            memo[s[r]] += 1
            r += 1
            if len(memo) > 2:
                memo[s[l]] -= 1
                if not memo[s[l]]: del memo[s[l]]
                l += 1
        return r-l
