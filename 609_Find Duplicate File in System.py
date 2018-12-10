class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        memo = collections.defaultdict(list)
        for comb in paths:
            lst = comb.split()
            path = lst[0]
            for i in range(1, len(lst)):
                file_list = lst[i].split("(")
                name, cont = file_list[0],file_list[1][:-1]
                memo[cont].append(path + "/" + name)
        return [group for group in memo.values() if len(group) > 1]
