class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1: return True
        l, r = 0, len(s1)
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2[l:r])
        if count1 == count2: return True
        while r < len(s2):
            count2[s2[r]] += 1
            count2[s2[l]] -= 1
            if not count2[s2[l]]: del count2[s2[l]]
            if count1 == count2: return True
            l+=1; r+=1
        return False
        
        # super slow
        # count1 = collections.Counter(s1)
        # l = len(s1)
        # for i in range(l-1, len(s2)):
        #     if count1 == collections.Counter(s2[i-l+1:i+1]): return True
        # return False
