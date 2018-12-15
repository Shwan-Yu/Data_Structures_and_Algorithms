class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def squareDigit(num):
            add = 0
            for char in str(num):
                add += int(char) ** 2
            return add
        
        memo = set()
        while n != 1:
            memo.add(n)
            n = squareDigit(n)
            if n in memo: return False
        return True
