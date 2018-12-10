class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): return s
        index, direction, lst = 0, 1, [""] * numRows
        for char in s:
            if index == 0: direction = 1
            elif index == numRows-1: direction = -1
            lst[index] += char
            index += direction
        return "".join(lst)
