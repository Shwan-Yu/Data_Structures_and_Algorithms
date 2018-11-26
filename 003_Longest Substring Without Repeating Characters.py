class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max_length, dup_char = 0, 0, {}
        for i, char in enumerate(s):
            if char in dup_char and start < dup_char[char]+1:
                start = dup_char[char]+1
            max_length = max(max_length, i-start+1)
            dup_char[char] = i
        return max_length
