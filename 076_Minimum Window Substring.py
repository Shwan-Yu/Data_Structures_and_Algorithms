class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right, res_l, res_r, min_len = 0, 0, 0, 0, float("inf")
        count_map = collections.defaultdict(int)
        for char in t: 
            count_map[char] += 1
        while right <= len(s):
            if all(map(lambda i: True if i <= 0 else False, count_map.values())):
                if (right - left) < min_len:
                    min_len = right - left
                    res_l, res_r = left, right
                if s[left] in count_map: 
                    count_map[s[left]] += 1
                left += 1
            else:
                if right == len(s): break
                if s[right] in count_map: 
                    count_map[s[right]] -= 1
                right += 1
        return s[res_l:res_r]
