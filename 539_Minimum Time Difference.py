class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # add minimum value also as the biggest one
        minutes = []
        for time in timePoints:
            lst = time.split(":")
            minutes.append(int(lst[0]) * 60 + int(lst[1]))
        minutes.sort()
        minutes.append(minutes[0] + 24*60)
        min_val = float("inf")
        for i in range(1, len(minutes)):
            min_val = min(min_val, minutes[i]-minutes[i-1])
        return min_val
