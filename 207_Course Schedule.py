class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for count in range(numCourses)]
        visited = [0 for count in range(numCourses)]
        
        for course, pre in prerequisites:
            graph[course].append(pre)
            
        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
