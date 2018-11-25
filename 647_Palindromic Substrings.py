class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        def countPal(s, l, r):
            count = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                count += 1; l-=1; r+=1
            return count
        res = 0
        for i in range(len(s)):
            res += countPal(s, i, i)
            res += countPal(s, i, i+1)
        return res
