class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            # "-1" is not digit, so use not in "+-*/"
            if s not in "+-*/": stack.append(int(s))
            else:
                num1, num2 = stack.pop(), stack.pop()
                if s == "+": stack.append(num1+num2)
                elif s == "-": stack.append(num2-num1)
                elif s == "*": stack.append(num1*num2)
                else: stack.append(int(float(num2)/float(num1)))
        return stack.pop()
