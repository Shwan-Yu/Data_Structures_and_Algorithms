class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        # s[0] != "0", str type
        # worst case O(3 ^ n)
        def backtracking(s, parts, path, res):
            if parts == 4:
                if s:
                    return
                res.append(path[:-1])
                return
            
            for i in range(1,4):
                if i <= len(s):
                    if i == 1:
                        backtracking(s[i:], parts+1, path+s[:i]+".",res)
                    elif s[0] != "0" and int(s[:i]) <= 255:
                        backtracking(s[i:], parts+1, path+s[:i]+".",res)

        res = []
        backtracking(s, 0, "", res)
        return res
