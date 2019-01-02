class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 0:i = 0; i:j = 1; j:k = 2
        # keep sorted before k
        
#         ijk
#         2   1   0   1   2 state
        
#         ij  k
#         2   1   0   1   2
        
#         i  jk
#         1   2   0   1   2 state
        
#         i   j   k
#         1   2   0   1   2
        
#             i   jk
#         0   1   2   1   2 state

        
        i = j = 0
        for k in range(len(nums)):
            val = nums[k]
            nums[k] = 2
            # modify j
            if val < 2:
                nums[j] = 1
                j += 1
            if val == 0:
                nums[i] = 0
                i += 1
        
        # slow, O(2n)
        # count = collections.Counter(nums)
        # i = 0
        # while i < len(nums):
        #     for val in range(3):
        #         for _ in range(count[val]):
        #             nums[i] = val
        #             i += 1
