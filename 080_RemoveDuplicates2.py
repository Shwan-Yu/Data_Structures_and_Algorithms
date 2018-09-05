class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return length
        tail = 1
        for i in range(2, length):
            if nums[i] != nums[tail] or nums[tail] != nums[tail - 1]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1
