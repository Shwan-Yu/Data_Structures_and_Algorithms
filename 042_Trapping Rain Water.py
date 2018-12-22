class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # first get the outer shape, then calculate water by bin
        def getShape(lst):
            max_h, res = 0, []
            for h in lst:
                max_h = max(h, max_h)
                res.append(max_h)
            return res
        
        left_h, right_h, sum_water = getShape(height), getShape(height[::-1])[::-1], 0
        for i, cur_h in enumerate(height):
            sum_water += min(left_h[i], right_h[i]) - cur_h
        return sum_water
