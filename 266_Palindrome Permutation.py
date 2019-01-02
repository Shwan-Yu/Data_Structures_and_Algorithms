class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # count = collections.Counter(s)
        # appears = 0
        # for times in count.values():
        #     if times%2 == 1: appears += 1
        #     if appears > 1: return False
        # return True
    
        count = collections.Counter(s)
        return sum(times%2==1 for times in count.values()) < 2
