class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # O(n^2)
        def cal_dist(a,b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2
        
        res = 0
        for p in points:
            dic = collections.defaultdict(int)
            for q in points:
                if q is not p: #this line is not neccessary
                    dist = cal_dist(p,q)
                    dic[dist] += 1 # we can also use dic[dist] = 1+dic.get(dist, 0)
            for key in dic:
                res += dic[key]*(dic[key]-1)
        return res
