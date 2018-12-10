class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res, path, inComment = [], "", False
        for line in source:
            i = 0
            while i < len(line):
                char = line[i]
                if char == "/" and i+1 < len(line) and line[i+1] == "/" and not inComment:
                    i = len(line)
                elif char == "/" and i+1 < len(line) and line[i+1] == "*" and not inComment:
                    inComment = True
                    i += 1
                elif char == "*" and i+1 < len(line) and line[i+1] == "/" and inComment:
                    inComment = False
                    i += 1
                elif not inComment:
                    path += char
                i += 1
            if path and not inComment:
                res.append(path)
                path = ""
        return res
