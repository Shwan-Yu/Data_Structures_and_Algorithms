class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        import collections
        self.tic_map = collections.defaultdict(list)
        for dep, arr in sorted(tickets)[::-1]:
            self.tic_map[dep].append(arr)
        self.res = []
        def getNext(dep):
            while self.tic_map[dep]:
                getNext(self.tic_map[dep].pop())
            self.res.append(dep)
            
        getNext("JFK")
        return self.res[::-1]
