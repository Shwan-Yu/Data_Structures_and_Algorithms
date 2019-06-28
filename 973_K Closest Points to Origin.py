class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappushpop
        res = []
        for point in points:
            # create a max heap where the max distance point is res[0]
            if len(res) < K:
                heappush(res, (-self.calDistance(point),point))
            # compare new point with max distance point in the heap
            elif self.calDistance(point) < -res[0][0]:
                heappushpop(res, (-self.calDistance(point),point))
        return zip(*res)[1]
        
    def calDistance(self, point):
        return (point[0]**2+point[1]**2)**0.5
