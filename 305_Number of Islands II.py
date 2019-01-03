# O(4*k)
class Union(object):
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.count = 0
        
    def add(self, tup):
        self.parent[tup] = tup
        self.size[tup] = 1
        self.count += 1
        
    def root(self, tup):
        while tup != self.parent[tup]:
            # change its parent to its parent's parent, then move tup to its parent
            self.parent[tup] = self.parent[self.parent[tup]]
            tup = self.parent[tup]
        return tup
        
    def union(self, tupi, tupj):
        i, j = self.root(tupi), self.root(tupj)
        if i == j: return
        # we want j to be the smallest one
        if self.size[i] < self.size[j]:
            i, j = j, i
        self.parent[j] = i
        self.size[i] += self.size[j]
        self.count -= 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        islands = Union()
        res = []
        for i, j in positions:
            if (i, j) not in islands.parent:
                islands.add((i,j))
                for di, dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if (di,dj) in islands.parent:
                        islands.union((i,j),(di,dj))
                res.append(islands.count)
        return res
        
