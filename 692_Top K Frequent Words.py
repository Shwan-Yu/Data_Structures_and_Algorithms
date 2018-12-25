class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # O(nlgn)
        count = collections.Counter(words).items()
        res = sorted(count, key = lambda x: (-x[1], x[0]))
        return zip(*res)[0][:k] # [i,2],[love,3] --> [i,love], [2,3]
    
        # O(n+klgk)
        count, dic = collections.Counter(words), collections.defaultdict(list)
        for word, c in count.items():
            dic[c].append(word)
        # from max possible count
        res = []
        for i in reversed(range(len(words))):
            if i in dic:
                for word in dic[i]:
                    res.append((i, word))
            if len(res) > k: break
        res_s = sorted(res, key = lambda x:(-x[0], x[1]))
        return zip(*res_s[:k])[1]
