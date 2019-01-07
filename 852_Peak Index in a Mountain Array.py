class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A)-1
        while l < r:
            mid = (l+r)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]: return mid
            elif A[mid] > A[mid-1]: l = mid+1
            elif A[mid] < A[mid-1]: r = mid
        return -1
