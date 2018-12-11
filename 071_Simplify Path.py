class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # ignore all dots and spaces, split remove all slash
        stack = [] 
        for p in path.split("/"):
            if p == "..": stack.pop() if stack else stack 
            elif p and p!= ".": stack.append(p)
        return "/" + "/".join(stack)
