class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = [char for char in s.strip().split(" ") if char][::-1]
        return " ".join(lst)
