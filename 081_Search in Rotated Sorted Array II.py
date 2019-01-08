class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 1 3 1 1 1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            if nums[l]<=nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return False
