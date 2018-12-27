class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy, O(n).
        # step0:
        # i    n_f
        # 2  3  1  2  3  
        # step1: current furthest point can reach in 1 step
        # i    c_f
        # 2  3  1  2  3
        # step1: current furthest point can reach in 1 step, and the furthest in 2 step (next)
        #    i c_f   n_f
        # 2  3  1  2  3
        # step2: get into step 2, add step and next become current.
        #       i    c_f
        # 2  3  1  2  3
        
        steps, cur_furthest, next_furthest = 0, 0, 0
        for i in range(len(nums)-1):
            next_furthest = max(next_furthest, i+nums[i])        
            if i == cur_furthest:
                steps += 1
                cur_furthest = next_furthest
        return steps
            
        # TLE BFS
        # q, memo, count = [(0, nums[0])], set([0]), 0
        # while q:
        #     newq = []
        #     for ind, max_jump in q:
        #         if ind == len(nums)-1: return count
        #         for d in range(1, max_jump+1):
        #             next_ind = ind+d
        #             if 0<=next_ind<len(nums) and next_ind not in memo:
        #                 newq.append((next_ind, nums[next_ind]))
        #                 memo.add(next_ind)
        #     q, count = newq, count+1
        # return -1
