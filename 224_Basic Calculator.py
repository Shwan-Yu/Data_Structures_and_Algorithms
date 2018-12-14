class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remember to reset num and last_sign, and res after append res
        last_sign, num, res, stack, s = 1, 0, 0, [], s+"+"
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                res += last_sign * num
                num = 0; last_sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append((res, last_sign))
                last_sign, res = 1, 0
            elif char == ")":
                res += last_sign * num
                before = stack.pop()
                res = res * before[1] + before[0]
                #don't need to reset last_sign because there will only be a new sign after )
                num = 0
        return res
