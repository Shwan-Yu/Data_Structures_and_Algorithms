class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack, res = [], 0
        for char in S:
            if char == "(": stack.append(char)
            elif char  == ")":
                if stack: stack.pop()
                else: res += 1
        return res + len(stack)
