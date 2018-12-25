class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(mlgk, m is the number of distinct, worse case m = n)
        from heapq import *
        count = collections.Counter(nums)
        res = []
        for num, c in count.items():
            # minheap
            if len(res) < k:
                heappush(res, (c, num))
            else:
                if res and c > res[0][0]: heappushpop(res, (c, num))
        return [heappop(res)[1] for i in range(k) if res]
        
        # nlgk
        # count = collections.Counter(nums)
        # return zip(*count.most_common(k))[0]
