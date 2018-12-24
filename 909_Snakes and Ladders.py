class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # BFS, first turn board into 1D array, then maintain a queue to do BFS
        # BFS:
        # 1. newq; 2. end case; 3. not moving forward cases 4. all this level case append in memo and newq; 5. q = newq, count += 1
        # O(V+E) = O(n^2 + 6 ^ moves) worst case
        n = len(board)
        memo, lst, moves = set(), [0], 0 #board start with square 1
        for i, row in enumerate(board[::-1]):
            lst.extend(row[::-1]) if i%2 else lst.extend(row)
        q = [1]
        s = 0
        while q:
            newq = []
            for start in q:
                if start == n*n: return moves
                for i in range(1,7):
                    if start+i <= n*n and start+i not in memo:
                        memo.add(start+i) # we cannot keep moving.
                        newq.append(start+i if lst[start+i] == -1 else lst[start+i])
            moves += 1
            q = newq
        return -1
