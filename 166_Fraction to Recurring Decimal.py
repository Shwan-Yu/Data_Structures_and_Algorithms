class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # get the ans and remainder, record it in a string, then using stack to track if repeating
        sign = "-" if numerator * denominator < 0 else ""
        ans, remain = divmod(abs(numerator), abs(denominator))
        if remain == 0: return sign + str(ans)
        res = [sign + str(ans) + "."]
        stack = []
        while remain not in stack:
            stack.append(remain)
            ans, remain = divmod(remain*10, abs(denominator))
            res.append(str(ans))
        res.insert(stack.index(remain)+1 ,"(")
        res.append(")")
        return "".join(res).replace("(0)", "")
