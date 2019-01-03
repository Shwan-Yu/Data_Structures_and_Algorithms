class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # follow up: if more s, preprocess the t, store all its index in a map, and do binary search for indexes
        # O(n)
        if s and not t: return False
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: 
                i+=1
            j+=1
        return True if i == len(s) else False
