class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left, right, res_l, res_r, min_len = 0, 0, 0, 0, float("inf")
        count = collections.Counter(t)
        while right <= len(s):
            if all(map(lambda i: True if i <= 0 else False, count.values())):
                if (right - left) < min_len:
                    min_len = right - left
                    res_l, res_r = left, right
                if s[left] in count: 
                    count[s[left]] += 1
                left += 1
            else:
                if right == len(s): break
                if s[right] in count: 
                    count[s[right]] -= 1
                right += 1
        return s[res_l:res_r]
                   
