class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # better: turn wordDict into a set, mind the index
        # O(mn) if can't break, O(mn * n) worst case
        def canBreak(s, wordDict):
            dp = [True]+[False]*len(s)
            for i in range(1, len(s)+1):
                for word in wordDict:
                    if dp[i-len(word)] and s[i-len(word):i] == word:
                        dp[i] = True
            return dp[-1]
        
        if not canBreak(s, wordDict): return []
        dp = [[""]]+[[]]*len(s)
        for i in range(1, len(s)+1):
            cur_res = []
            for j in range(0, i):
                cur_seq = s[j:i]
                if cur_seq in wordDict and len(dp[j]) > 0:
                    for comb in dp[j]:
                        cur_res.append(comb+" "+cur_seq if comb != "" else cur_seq)
            dp[i] = cur_res
        return dp[-1]
