class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m,n = len(image), len(image[0])
        
        def paint(i, j):
            if (i,j) in memo: return
            old_c = image[i][j]
            image[i][j] = newColor
            memo.add((i,j))
            nei = [(-1,0),(1,0),(0,-1),(0,1)]
            for d in nei:
                di, dj = i + d[0], j + d[1]
                if 0 <= di < m and 0 <= dj < n and image[di][dj] == old_c: paint(di, dj)
        
        if 0<=sr<m and 0<=sc<n:
            memo = set()
            paint(sr, sc)
        return image
