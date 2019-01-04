class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # a: (b, 2.0)
        # b: (a, 0.5), (c, 3.0)
        # c: (b, 0.3333)
        # if numerator == denominator, return res. a, c: (a,1.0)->(b,2.0)->(c,6.0), we find c
        def findVal(query):
            i, j = query
            if i not in dic or j not in dic: return -1.0
            q, memo = [(i, 1.0)], {i}
            while q:
                newq = []
                for numer, res in q:
                    if numer == j: return res
                    for denom, val in dic[numer]:
                        if denom not in memo:
                            newq.append((denom, res*val))
                            memo.add(denom)
                q = newq
            return -1.0
                    
        dic  = collections.defaultdict(list)
        for eq, val in zip(equations, values):
            i, j  = eq
            dic[i].append((j, val))
            dic[j].append((i, 1/val))
            
        return [findVal(query) for query in queries]
