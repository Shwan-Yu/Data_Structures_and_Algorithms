class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        length = len(nums)
        lo, hi = 0 ,length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            m = nums[mid]
            if m == target:
                break
            elif m < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if m != target:
            return [-1, -1]
        lo = hi = mid
        while lo > 0 and nums[lo - 1] == target:
            lo -= 1
        while hi < length - 1 and nums[hi + 1] == target:
            hi += 1
        return [lo, hi]
            
