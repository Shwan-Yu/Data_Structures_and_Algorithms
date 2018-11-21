class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        e_map = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                e_map[account[j]].append(i)
        memo = [False] * len(accounts)
        
        def combineEmail(i, path):
            if not memo[i]:
                memo[i] = True
                for j in range(1, len(accounts[i])):
                    email = accounts[i][j]
                    path.add(email)
                    for nei in e_map[email]:
                        if not memo[nei]: combineEmail(nei, path)
      
        res = []
        for i, account in enumerate(accounts):
            if not memo[i]:
                path = set()
                name = account[0]
                combineEmail(i, path)
                res.append([name]+sorted(path))
        return res
