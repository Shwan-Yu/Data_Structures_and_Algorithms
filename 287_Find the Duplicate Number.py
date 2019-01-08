class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return head
    
        # memo = set()
        # for num in nums:
        #     if num in memo: return num
        #     memo.add(num)
        # return -1
