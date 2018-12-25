class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # O(klgk) heappush and heappop both lg(n).
        from heapq import *
        heap = []
        for numi in nums1:
            for numj in nums2:
                # maxheap
                if len(heap) < k: heappush(heap, (-(numi+numj), [numi, numj]))
                else:
                    # check if heap is empty
                    if heap and numi+numj < -heap[0][0]:
                        heappushpop(heap, (-(numi+numj),[numi, numj]))
                    else: break
        return [heappop(heap)[1] for i in range(k) if heap]
