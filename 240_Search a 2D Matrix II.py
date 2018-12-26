class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # start from top right, go down or left
        # O(m+n) worst case
        if not matrix: return False
        start_r, start_c = 0, len(matrix[0])-1
        while start_r < len(matrix) and start_c >= 0:
            val = matrix[start_r][start_c] 
            if val == target: return True
            elif val < target: start_r+=1
            else: start_c -= 1
        return False
