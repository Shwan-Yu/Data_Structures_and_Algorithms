# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Because the celebrity doesn't know anyone, so if A knows B, then A is not the celebrity.
        # Because anyone knows the celebrity, so if A doesn't know B, then B is not the celebrity.
        check = 0
        for i in range(1, n):
            if knows(check, i):
                check = i
        
        # right now check is the only one that may be the celebrity.
        # if anyone doesn't know him, or he knows anyone other than himself, he's not the celebrity.
        if any(not knows(i, check) or knows(check, i) for i in range(n) if i != check):
            return -1
        return check
