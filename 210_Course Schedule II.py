class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        c_map = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            c_map[course].append(pre)
        memo = [0] * numCourses
        self.res = []
        def checkPre(i):
            if memo[i] == 1: return True
            if memo[i] == -1: return False
            memo[i] = -1
            for pre in c_map[i]:
                if not checkPre(pre): return False
            self.res.append(i)
            memo[i] = 1
            return True
        
        for i in range(numCourses):
            if not checkPre(i): return []
        return self.res
