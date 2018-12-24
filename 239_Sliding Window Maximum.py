class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        if not k or not nums: return [] # because we start from next possible window
        res, dq = [], deque()
        for i in range(k):
            # only keep potential largest element's indexes in the dq
            while dq:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else: break
            dq.append(i)
        res.append(nums[dq[0]])
        l, r = 1, k
        while r < len(nums):
            if dq[0] < l: dq.popleft()
            while dq:
                if nums[r] > nums[dq[-1]]:
                    dq.pop()
                else: break
            dq.append(r)
            res.append(nums[dq[0]])
            l+=1; r+=1
        return res
            
                    
        
        # O(n*k)
        # if not k: return []
        # l, r, res = 0, k-1, []
        # while r < len(nums):
        #     res.append(max(nums[l:r+1]))
        #     l+=1; r+=1
        # return res
