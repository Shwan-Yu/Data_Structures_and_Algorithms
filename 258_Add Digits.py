class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            res = 0
            while num > 0:
                res += num%10
                num //= 10
            num = res
        return num
    
        # if num == 0 : return 0
        # else:return (num - 1) % 9 + 1
