class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        # first two check x, other two check y
        return rec2[2] > rec1[0] and rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec2[3] > rec1[1]
