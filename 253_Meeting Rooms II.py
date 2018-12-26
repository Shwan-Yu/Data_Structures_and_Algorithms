# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # Store the first end time using heap, when new meeting, check if first end time's room is available.
        # O(nlgk), k is the number of the rooms
        from heapq import *
        intervals.sort(key = lambda x: x.start)
        heap = []
        for m in intervals:
            if heap and m.start >= heap[0]:
                heappushpop(heap, m.end)
            else:
                heappush(heap, m.end)
        return len(heap)
