class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r, memo = 0, len(num)-1, (("0","0"), ("1","1"),("6","9"),("9","6"),("8","8"))
        while l <= r:
            if (num[l],num[r]) not in memo: return False
            l+=1; r-=1
        return True
    
        # dic = {"0":"0", "1":"1","6":"9","9":"6","8":"8"}
        # for digit1, digit2 in zip(num, num[::-1]):
        #     if digit1 not in dic or dic[digit1] != digit2: return False
        # return True
