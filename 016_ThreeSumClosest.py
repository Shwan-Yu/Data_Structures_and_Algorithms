class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        length = len(nums)
        nums.sort()
        result = float('inf')
        
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == target:
                    return threeSum
                if abs(threeSum - target) < abs(result - target):
                    result = threeSum
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
        return result
