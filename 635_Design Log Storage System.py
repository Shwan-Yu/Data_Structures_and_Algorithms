class LogSystem(object):

    def __init__(self):
        self.log = []
        self.index = {"Year":4, "Month":7, "Day":10, "Hour":13, "Minute":16, "Second":19}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.log.append((id, timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        i = self.index[gra]
        s = s[:i]
        e = e[:i]
        return [tid for tid, time in self.log if s<=time[:i]<=e]
