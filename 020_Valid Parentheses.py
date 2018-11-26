class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict, stack = {"(":")","[":"]","{":"}"}, []
        for char in s:
            if char in ["(","[","{"]: stack.append(char)
            elif not stack or char != dict[stack.pop()]: return False
        return True if not stack else False
