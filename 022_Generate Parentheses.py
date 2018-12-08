class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #O(2 ^ n)
        def backtracking(leftPar, rightPar, path, res):
            #backtracking
            if leftPar > rightPar or leftPar < 0 or rightPar < 0: 
                return
            if leftPar == 0 and rightPar == 0:
                res.append(path)
                return
            backtracking(leftPar-1,rightPar, path+ "(", res)
            backtracking(leftPar,rightPar-1, path+ ")", res)
        
        s, res = "", []
        backtracking(n, n, "", res)
        return res
        
