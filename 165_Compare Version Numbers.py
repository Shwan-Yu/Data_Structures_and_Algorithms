class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        for i in range(max(len(version1), len(version2))):
            # complete with 0 because we can have 1.00000 and 1.00 or 1.0001 and 1.00
            v1 = version1[i] if i < len(version1) else 0
            v2 = version2[i] if i < len(version2) else 0
            if v1 > v2: return 1
            elif v1 < v2: return -1
        return 0
