class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [()]
        # for num in nums:
        #     res = set(tuple(prev[:i]+tuple([num])+prev[i:]) for prev in res for i in range(len(prev)+1))
        # return map(list, res)
    
        res = [()]
        for num in nums:
            new_res = set()
            for prev in res:
                for i in range(len(prev)+1):
                    new_res.add(tuple(prev[:i]+tuple([num])+prev[i:]))
            res = new_res
        return map(list, res)
