class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # sliding window
        # normal
        # 1. update dict right
        # 2. meets the condition, updata dict left and move left
        # 3. move right
        
        # one less right first, update dic[s[r]] at every beginning, dic[s[l]] at every end
        # dic[s[r]] not dic[r]
        if len(s) < len(p): return []
        l, r, res = 0, len(p)-1, []
        count1 = collections.Counter(p)
        count2 = collections.Counter(s[l:r])
        while r < len(s):
            count2[s[r]] += 1
            if count1 == count2: res.append(l)
            count2[s[l]] -= 1           
            if not count2[s[l]]: del count2[s[l]]
            l+=1; r+=1
        return res
