class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]
    
    # brute force O(n) because of insert
#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.lst = sorted(nums, reverse = True)
#         self.k = k

#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         self.lst.insert(self.BS(val), val)
#         return self.lst[self.k - 1]
    
#     def BS(self, val):
#         # search insert position
#         l, r = 0, len(self.lst)-1
#         while l <= r:
#             mid = (l+r) // 2
#             if self.lst[mid] == val: return mid
#             if self.lst[mid] > val: l = mid+1
#             else: r = mid-1
#         return l


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
