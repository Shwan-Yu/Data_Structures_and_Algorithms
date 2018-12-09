class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #unicode
        res, carry = "", 0
        while len(a) != len(b):
            if len(a)<len(b): a = "0" + a
            else: b = "0" + b  
        for i in reversed(range(len(a))):
            total = ord(a[i]) - ord("0") + ord(b[i]) - ord("0") + carry
            res = `total%2`  + res
            carry = total // 2
        if carry: res = "1" + res
        return res
