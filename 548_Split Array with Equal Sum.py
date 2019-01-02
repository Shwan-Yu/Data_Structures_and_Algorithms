class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n^2
        # divide into two equal sum subarrays, record all possibilities
        def divide(arr):
            total, res = sum(arr), set()
            # sum of left half + sum of left half + arr[i] = total, then total-arr[i] = 2* sum of left half
            for i in range(1, len(arr)):
                arr[i] += arr[i-1]
            for i in range(1, len(arr)-1):
                if arr[i-1] + arr[i] == total: res.add(arr[i-1])
            return res
            
        if len(nums)<= 6: return False
        return any(divide(nums[:mid]) & divide(nums[mid+1:]) for mid in range(3, len(nums)-3))
