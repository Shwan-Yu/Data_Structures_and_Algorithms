class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Using i-1 situation result and i-2 situation result to generate new result. The space complexity can be easily reduced by just changing a few lines to just record i-1, i-2.
I think the time complexity would be O(n^2).

        odd_mid, even_mid, dp = ["0","1","8"], ["00","11","69","88","96"], [[]] * (n+1)
        if n == 1: return odd_mid
        if n == 2: return even_mid[1:]
        dp[1], dp[2] = odd_mid, even_mid[1:]
        for i in range(3, n+1):
            if i % 2 == 1:
                mid = (len(dp[i-1][0])-1)//2
                dp[i] = [num[:mid+1]+ mid_str + num[mid+1:] for num in dp[i-1] for mid_str in odd_mid]
            else:
                mid = (len(dp[i-2][0])-1)//2
                dp[i] = [num[:mid+1]+ mid_str + num[mid+1:] for num in dp[i-2] for mid_str in even_mid]
        return dp[n]
        
        # We can just check needed i
        # odd_mid, even_mid = ["0","1","8"], ["00","11","69","88","96"]
        # if n == 1:
        #     return odd_mid
        # if n == 2:
        #     return even_mid[1:]
        # if n % 2:
        #     pre, midCandidate = self.findStrobogrammatic(n-1), odd_mid
        # else: 
        #     pre, midCandidate = self.findStrobogrammatic(n-2), even_mid
        # premid = (n-1)//2
        # return [p[:premid] + c + p[premid:] for p in pre for c in midCandidate ]
