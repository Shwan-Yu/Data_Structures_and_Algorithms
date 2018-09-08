class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi ) // 2
            m = nums[mid]
            if m == target:
                return mid
            elif m > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
