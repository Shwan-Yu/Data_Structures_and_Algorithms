class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        i, carry, res = 0, 0, ""
        while i < max(len(a), len(b)) or carry:
            v1 = v2 = 0
            if i < len(a):
                v1 = ord(a[i]) - ord("0")
            if i < len(b):
                v2 = ord(b[i]) - ord("0")
            carry, remainder = divmod(v1+v2+carry, 2)
            res = str(remainder) + res
            i += 1
        return res
    
        #unicode
#         res, carry = "", 0
#         while len(a) != len(b):
#             if len(a)<len(b): a = "0" + a
#             else: b = "0" + b  
#         for i in reversed(range(len(a))):
#             total = ord(a[i]) - ord("0") + ord(b[i]) - ord("0") + carry
#             res = `total%2`  + res
#             carry = total // 2
#         if carry: res = "1" + res
#         return res
