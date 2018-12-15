class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, n):
            if dp[i]:
                # right boundary is exclusive, so + 1
                for j in range(i, ((n-1)//i) + 1):
                    dp[i*j] = False
        return sum(dp)
        
        
        # Brute Force
        # def isPrime(num):
        #     for i in range(2, num):
        #         if num % i == 0: return False
        #     return True
        # count = 0
        # for i in range(2, n):
        #     if isPrime(i): count += 1
        # return count
