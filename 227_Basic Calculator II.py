class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, pre_op, num = [], "+", 0
        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            # should finish the last operation, so use if not elif.
            if char in "+-*/" or i == len(s)-1:
                if pre_op == "+": stack.append(num)
                elif pre_op == "-": stack.append(-num)
                elif pre_op == "*": stack.append(stack.pop() * num)
                else: stack.append(int(stack.pop() / float(num)))
                num, pre_op = 0, char
        return sum(stack)
