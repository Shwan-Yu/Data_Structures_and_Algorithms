class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for char in str:
            res += chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char
        return res
