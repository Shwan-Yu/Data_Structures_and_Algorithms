class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        short = min(strs, key = len)
        for i, char in enumerate(short):
            for word in strs:
                if word[i] != char: return short[:i]
        return short
