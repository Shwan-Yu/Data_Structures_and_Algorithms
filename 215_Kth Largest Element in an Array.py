class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(nlgk)
        from heapq import *
        heap = []
        for n in nums:
            # MinHeap
            if len(heap) < k: heappush(heap, n)
            else:
                if heap and n > heap[0]: heappushpop(heap, n)
        return heap[0]
