class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        repeat = ""
        
        for char in s:
            if char.isdigit():
                repeat += char
            elif char == "[":
                stack.append(["", int(repeat)])
                repeat = ""
            elif char == "]":
                seq, rep = stack.pop()
                stack[-1][0] += seq * rep
            else:
                stack[-1][0] += char
                
        return stack[0][0]
