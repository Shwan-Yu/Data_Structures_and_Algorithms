class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        # O(K*n^2) worst case, keep adding the probability of getting out of the board
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        memo, out_board_p = {(r, c): 1}, 0
        # for each step we will create a new dict to record the onboard coordinates and their probabilities.
        for step in range(K):
            next_memo = collections.defaultdict(int)
            for (i, j), prob in memo.items():
                for d in moves:
                    di, dj = i+d[0], j+d[1]
                    # if the next step is on the board, we record it for next step's calculation
                    if 0<=di<N and 0<=dj<N:
                        next_memo[(di,dj)] += prob * 0.125
                    # if the next step is not on the board, we sum it to our accumulate probability of out-board.
                    else:
                        out_board_p += prob * 0.125
            memo = next_memo
        # the on-board prob = 1 - the accumulate out board prob
        return 1-out_board_p
        
        # total 8^k, worse case O(8^k) TLE
        # moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        # # don't need the memo because duplicate moves are count as different moves
        # q, steps = [(r,c)], 0
        # # or while True
        # while q:
        #     if steps == K: return float(len(q)) / (8**K)
        #     newq = []
        #     for i, j in q:
        #         for d in moves:
        #             di, dj = i+d[0], j+d[1]
        #             if 0<=di<N and 0<=dj<N:
        #                 newq.append((di, dj))
        #     steps, q = steps+1, newq
        # return 0.0
