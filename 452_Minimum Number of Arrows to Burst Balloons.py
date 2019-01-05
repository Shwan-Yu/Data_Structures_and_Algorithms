class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # [1, 6],[2, 8],[7, 12],[10, 16]
        # if overlapping, can use one shot. So we just count the overlapping.
        if not len(points): return 0
        points.sort(key = lambda x: x[0])
        count, overlapping = 1, points[0]
        for i in range(1, len(points)):
            ballon = points[i]
            if ballon[0] <= overlapping[1]:
                start, end = max(ballon[0], overlapping[0]), min(ballon[1], overlapping[1])
                overlapping = [start, end]
            else:
                count += 1
                overlapping = points[i]
        return count
