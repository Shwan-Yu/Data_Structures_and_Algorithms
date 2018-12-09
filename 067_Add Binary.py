class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, carry = "", 0
        while len(a) != len(b):
            if len(a)<len(b): a = "0" + a
            else: b = "0" + b  
        for i in reversed(range(len(a))):
            total = int(a[i]) + int(b[i]) + carry
            res = str(total%2)  + res
            carry = total // 2
        if carry: res = "1" + res
        return res
