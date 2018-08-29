class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        the area is only determined by the shorter side, so the area will only be bigger if the shorter side becomes longer.
        """
        left = 0
        right = len(height) - 1
        area = 0
        
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
