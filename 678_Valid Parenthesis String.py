class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == "(" or char == "*": stack.append(char)
            else:
                if not stack: return False
                stack.pop()
        stack = []
        for char in reversed(s):
            if char == ")" or char == "*": stack.append(char)
            else:
                if not stack: return False
                stack.pop()
        return True
