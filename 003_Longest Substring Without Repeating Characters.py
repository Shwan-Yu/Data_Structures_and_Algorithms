class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        l, r, count = 0, 0, collections.defaultdict(int)
        while r < len(s):
            count[s[r]] += 1
            r += 1
            if not all(map(lambda i: True if i<=1 else False, count.values())):
                count[s[l]] -= 1
                l += 1
        return r-l
    
    
#         start, max_length, dup_char = 0, 0, {}
#         for i, char in enumerate(s):
#             if char in dup_char and start < dup_char[char]+1:
#                 start = dup_char[char]+1
#             max_length = max(max_length, i-start+1)
#             dup_char[char] = i
#         return max_length
