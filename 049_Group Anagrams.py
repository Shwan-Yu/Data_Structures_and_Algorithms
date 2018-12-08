class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for string in strs:
            key = tuple(sorted(string))
            dic[key] = dic.get(key, []) + [string]
        return dic.values()
