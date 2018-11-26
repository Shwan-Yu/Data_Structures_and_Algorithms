class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # O(1)
        digits = {i for i in time if i != ":"}
        h, m = time.split(":")
        while True:
            h, m = (str(int(h)+1), "00") if m == "59" else (h, str(int(m)+1))
            if int(h) > 23: h = "00" 
            if len(h) == 1: h = "0" + h
            if len(m) == 1: m = "0" + m
            if set(h+m).issubset(digits): return h +":"+ m
