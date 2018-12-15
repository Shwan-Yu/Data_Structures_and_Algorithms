class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        one = [1]
        i, j, carry, res = len(digits)-1, 0, 0, []
        while i>=0 or j>=0 or carry:
            v1=v2=0
            if i>=0: v1 = digits[i]
            if j>=0: v2 = one[j]
            carry, digit = divmod(v1+v2+carry, 10)
            res.append(digit)
            i-=1;j-=1
        return res[::-1]
