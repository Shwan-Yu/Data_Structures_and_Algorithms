class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # from right to left
        zipped = sorted(zip(indexes, sources, targets), reverse = True)
        for index, source, target in zipped:
            if S[index: index+len(source)] == source: S = S[:index] + target + S[index+len(source):]
        return S
