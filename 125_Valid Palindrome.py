class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # in-place
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1; r -= 1
        return True
        
        # short and fast
        # lst = [char.lower() for char in s if char.isalnum()]
        # return lst == lst[::-1]
