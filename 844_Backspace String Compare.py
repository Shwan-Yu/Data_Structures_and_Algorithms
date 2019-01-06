class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, stackS, stackT = 0, [], []
        for char in S:
            if char == "#":
                if stackS: stackS.pop()
            else:
                stackS.append(char)
        for char in T:
            if char == "#":
                if stackT: stackT.pop()
            else:
                stackT.append(char)
        return stackS == stackT
