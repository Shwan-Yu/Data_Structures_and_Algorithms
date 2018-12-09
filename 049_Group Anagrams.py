class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            dic[key].append(string)
        return dic.values()
