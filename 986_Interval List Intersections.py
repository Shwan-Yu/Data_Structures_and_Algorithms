class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        i, j = 0, 0
        # if j out of range
        # if no intersection
        # what to keep: [0, 2] [1, 5] --> [1, 2]
        while i < len(A):
            if j >= len(B): break
            if A[i][0] > B[j][1]: j += 1
            elif A[i][1] < B[j][0]: i += 1
            else:
                # should think about when equals [2, 5], [1, 5] --> [2, 5]
                if A[i][1] < B[j][1]:
                    res.append([max(A[i][0], B[j][0]), A[i][1]])
                    i += 1
                else:
                    res.append([max(A[i][0], B[j][0]), B[j][1]])
                    j += 1
        return res
