class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(S)
        res = 0
        for char in J:
            res += c.get(char, 0)
        return res
