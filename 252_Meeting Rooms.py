# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        lst = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(lst)):
            if lst[i].start < lst[i-1].end: return False
        return True
