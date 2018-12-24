        if not k or not nums: return [] # because we start from next possible window
        res, dq = 0, k-1, [], deque()
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
