class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1 == p2 == p3 == p4: return False
        def d(m, n):
            return (m[0] - n[0])**2 + (m[1] - n[1])**2
        dist = sorted([d(p1,p2),d(p1,p3),d(p1,p4),d(p2,p3),d(p2,p4),d(p3,p4)])
        if dist[0] == dist[1] == dist[2] == dist[3]:
            if dist[4] == dist[5]: return True
        return False
