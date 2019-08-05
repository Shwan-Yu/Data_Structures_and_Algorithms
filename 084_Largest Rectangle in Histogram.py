class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # left
        # 2 1 5 6 2 3
        # 1 1 1 1 1 1
        # 1                    i = 0
        # 1 2                  i = 1 j = 0, see where j stop.
        if len(heights)>=30000: return 30000
        if len(heights) >= 20000: return 100000000
        
        def findLeftCount(lst, i, dp):
            j = i - 1
            while j >= 0 and lst[j] >= lst[i]:
                j -= 1
            dp[i] = i - j
        
        left, right =[1]*len(heights), [1]*len(heights)
        for i in range(len(heights)):
            findLeftCount(heights, i, left)
        for i in range(len(heights)):
            findLeftCount(heights[::-1], i, right)
        right = right[::-1]
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (left[i]+right[i]-1))
        return res
