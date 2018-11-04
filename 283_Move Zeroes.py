class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tail = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[tail], nums[i] = nums[i], nums[tail]
                tail += 1
