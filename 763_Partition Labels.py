class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic, res, l, r = {}, [], 0, 0
        for i, char in enumerate(S):
            # get the rightest index of each letter
            dic[char] = i
        for i, char in enumerate(S):
            # get the right boundary we at least need to reach
            r = max(r, dic[char])
            if i == r:
                # append the length and move left to next chunk
                res.append(r-l+1)
                l = i+1
        return res
