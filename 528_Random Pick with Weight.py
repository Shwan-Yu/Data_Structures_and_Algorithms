class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
#         0 0 0 1 2 2
        
#         0 1 2
#         3 1 2

#         3 4 6
        
#         choice 1-3: 0, choice 4: 1, choice 5-6: 2
        self.w = w
        self.total_weights = sum(self.w)
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.total_weights)
        l, r = 0, len(self.w)-1
        while l < r:
            mid = (l+r)//2
            if rand<=self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l
    
# TLE  
# class Solution(object):
#     import random
#     def __init__(self, w):
#         """
#         :type w: List[int]
#         """
#         self.pool = []
#         for num, weight in enumerate(w):
#             for i in range(weight): self.pool.append(num)

#     def pickIndex(self):
#         """
#         :rtype: int
#         """
#         return random.choice(self.pool)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
