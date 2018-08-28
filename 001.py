class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_index = index, value for value, index in enumerate(nums)
        nums_with_index.sort()
        start, end  = 0, len(nums) - 1
        while start < end:
            curr_sum = nums_with_index[start][0] + nums_with_index[end][0]
            if curr_sum == target:
                return (nums_with_index[start][1], nums_with_index[end][1])
            elif curr_sum < target:
                start += 1
                pass
            else:
                end -= 1
                pass
            pass
        return None
