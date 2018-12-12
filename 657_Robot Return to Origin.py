class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
        
        # x, y, dic = 0, 0, {"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}
        # for move in moves:
        #     x, y = x+dic[move][0], y+dic[move][1]
        # return True if x == y == 0 else False
