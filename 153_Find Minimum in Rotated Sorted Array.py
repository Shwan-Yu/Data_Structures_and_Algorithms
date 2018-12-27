class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if mid > right: 4 5 6 1 2, means that all the left are big numbers, drop all of them.
        # if mid <= right: 7 1 2 3 4 means that all the right are in order, keep reducing right to get the smallest.
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[r]<nums[mid]: l = mid+1
            else: r = mid
        return nums[l]
