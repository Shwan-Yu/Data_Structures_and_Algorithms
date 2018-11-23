class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        res = ""
        #return the max palidromic substring
        def paliSub(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            #odd case
            sub = paliSub(s, i, i)
            if len(sub) > len(res): res = sub
            #even case
            sub = paliSub(s, i, i+1)
            if len(sub) > len(res): res = sub
        return res
