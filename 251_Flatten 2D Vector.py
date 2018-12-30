class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.row = self.col = 0

    def next(self):
        """
        :rtype: int
        """
        # write or not write this line depending whether we call hasNext before next everytime.
        # if self.hasNext:
        res = self.vec[self.row][self.col]
        self.col += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row, self.col = self.row+1, 0
        return self.row < len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
