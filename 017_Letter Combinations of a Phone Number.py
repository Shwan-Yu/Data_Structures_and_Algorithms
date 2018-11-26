class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # O(4^n)
        if not digits: return []
        res, dic = [], {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(s, index, path, res):
            if len(path) == len(s):
                res.append(path)
                return
            for i in range(index, len(s)):
                for char in dic[s[i]]:
                    dfs(s, i+1, path+char,res)
        
        dfs(digits, 0, "", res)
        return res
