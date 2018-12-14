class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # same as the add linked list
        res, carry, i, j = "", 0, len(num1)-1, len(num2)-1
        while i>=0 or j>=0 or carry:
            v1 = v2 = "0"
            if i>=0:
                v1 = num1[i]
            if j>=0:
                v2 = num2[j]
            add = ord(v1)-ord("0") + ord(v2)-ord("0") + carry
            carry = add // 10
            res = str(add%10) + res
            i-=1;j-=1
        return res
