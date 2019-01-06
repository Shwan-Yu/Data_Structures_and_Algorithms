class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # just count all the edge positions, use the most frequent one
        count = collections.defaultdict(int)
        for row in wall:
            edge = 0
            # remove the right edge
            for brick in row[:-1]:
                edge += brick
                count[edge] += 1
        # count.values() might be empty because we delete the last element, so if there is just one element in a row, max would return an error. Or initialize count with a 0.
        return len(wall) - max(count.values() + [0])
