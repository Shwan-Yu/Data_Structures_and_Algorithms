class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # store them in groups
        if not matrix: return []
        groups = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                groups[i+j].append(matrix[i][j])
        res = []
        for k, v in groups.items():
            if k % 2 == 0: res.extend(v[::-1])
            else: res.extend(v)
        return res
