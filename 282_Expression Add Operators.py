class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # O(3^n*n!)
        # Exception: in 106, 1*06 doesn't count
        if not num: return []
        def dfs(num, prev, cur, path, res):
            # use all char in num and make cur == target
            if not num and cur == target:
                res.append(path)
                return
            for i in range(1, len(num)+1):
                val = num[:i]
                if i == 1 or (i > 1 and num[0] != "0"):
                    dfs(num[i:], int(val), cur+int(val), path+"+"+val, res)
                    dfs(num[i:], -int(val), cur-int(val), path+"-"+val, res)
                    # a little bit different when multiplying, already add prev before, so subtract it and add new prev
                    dfs(num[i:], prev*int(val), cur-prev+prev*int(val), path+"*"+val, res)
            
        res = []
        # handle the starting element: it can only be pos to start (between the digit), and can be several chars.
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # 051, we can only start with 0, not 05.
                start_val = num[:i]
                dfs(num[i:], int(start_val),int(start_val), start_val, res)
        return res
