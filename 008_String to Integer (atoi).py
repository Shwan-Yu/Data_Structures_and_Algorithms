class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        lst, res = list(str.strip()), 0
        if len(lst) == 0: return 0
        sign = -1 if lst[0] == "-" else 1
        if lst[0] in ["-", "+"]: del lst[0]
        for char in lst:
            if not char.isdigit(): break
            res = res * 10 + ord(char) - ord("0")   
        return max(-2**31, min(2**31-1, sign * res))
