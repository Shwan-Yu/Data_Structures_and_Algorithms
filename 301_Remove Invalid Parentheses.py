class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # O(n) check
        def isValid(s):
            stack = []
            for char in s:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    if not stack: return False
                    stack.pop()
            return True if not stack else False
        # n is checking and creating time, C(n,n) is from n pick n elements.
        # T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1)
        q, res, find_in_this_level = {s}, [], False
        while q:
            newq = set()
            for case in q:
                if isValid(case):
                    res.append(case)
                    find_in_this_level = True
                elif not find_in_this_level:
                    newq |= {case[:i]+case[i+1:] for i in range(len(case))}
            if find_in_this_level: return res
            q = newq
        return -1
