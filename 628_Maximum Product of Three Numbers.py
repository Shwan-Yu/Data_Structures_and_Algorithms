class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
        
        # large, small = heapq.nlargest(3,nums), heapq.nsmallest(2,nums)
        # return max(large[0]*large[1]*large[2], large[0]*small[0]*small[1])
