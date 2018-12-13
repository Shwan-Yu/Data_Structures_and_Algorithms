class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S: return T
        count, res = collections.Counter(T), ""
        for char in S:
            if char in count: 
                res += char * count[char]
                del count[char]
        for char in count.keys():
            res += char * count[char]
        return res
