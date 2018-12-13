class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # if larger and add 1 A and didn't work, then -1
        i, mul_A = 0, ""
        while len(B) > len(mul_A):
            mul_A += A; i += 1
            if B in mul_A: return i
        if B in mul_A + A:
            return i+1
        return -1
