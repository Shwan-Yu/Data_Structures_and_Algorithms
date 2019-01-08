class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # dividing coordinates by 3 to separate them into 9 small box
        # small: (val, i, j); row: (val, i, "row"); col: (val, j, "col")
        memo = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".": continue
                if (val, i//3, j//3) in memo or (val, i, "row") in memo or (val, j, "col") in memo: return False
                memo |= {(val, i//3, j//3), (val, i, "row"), (val, j, "col")}
        return True
