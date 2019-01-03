class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import *
        # put all first column in, we do it by row because next row is always bigger than this one. Start from col 0 and every time check the next col.
        heap = [(row[0], r, 0) for r, row in enumerate(matrix)]
        # pop the first k-1 elements, we get the kth
        for i in range(k-1):
            # don't pop it before processing, use heap[0]
            val, row, col = heap[0]
            # everytime, no matter we push in or not, we pop one every time
            if col+1 < len(matrix[row]):
                heappushpop(heap, (matrix[row][col+1], row, col+1))
            else:
                heappop(heap)
        return heap[0][0]
