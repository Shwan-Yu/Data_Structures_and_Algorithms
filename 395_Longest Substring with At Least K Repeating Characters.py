class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # O(n * 1) we only have to do at most 26 split, each worst case O(n) time
        # divide and conquer
        # base case
        if len(s) < k: return 0
        # else
        for char in set(s):
            # result would not contain the char that is less than k
            if s.count(char) < k:
                return max(self.longestSubstring(substr, k) for substr in s.split(char))
        return len(s)
