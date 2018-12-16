class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # each digit is a 26 ary digit, from 0-25: "25 1 14 10 23"
        res = ""
        while n > 0:
            n -= 1
            res = chr(n%26+ord("A")) + res
            n /= 26
        return res
        
        # self-written
        # ans, remainder = divmod(n, 26)
        # if remainder == 0: ans, remainder = ans-1, remainder+26
        # res = chr(remainder+ord("A")-1)
        # while ans > 26:
        #     ans, remainder = divmod(ans, 26)
        #     if remainder == 0: ans, remainder = ans-1, remainder+26
        #     res = str(chr(remainder+ord("A")-1)) + res
        # return chr(ans+ord("A")-1) + res if ans else res
