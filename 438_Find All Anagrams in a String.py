class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # sliding window
        if len(p) > len(s): return []
        r, res = len(p)-1, []
        count = collections.Counter(p)
        for i in range(len(p)-1):
            if s[i] in count: count[s[i]] -= 1
        while r < len(s):
            if s[r] in count: count[s[r]] -= 1
            if all(map(lambda i: True if i<=0 else False, count.values())):
                res.append(r-len(p)+1)
            if s[r-len(p)+1] in count: count[s[r-len(p)+1]] += 1
            r += 1
        return res
