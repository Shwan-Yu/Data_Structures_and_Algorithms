class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op not in "+DC": stack.append(int(op))
            elif op == "+": stack.append(stack[-1]+stack[-2])
            elif op == "C": stack.pop()
            else: stack.append(stack[-1]*2)
        return sum(stack)
                    
