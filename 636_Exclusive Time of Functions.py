class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # if start, then prev start at very first of start time
        # if end, then prev start at very first of the next second
        # +=
        res = [0] * n
        prev, stack = 0, []
        for log in logs:
            func, sta_or_end, time = log.split(":")
            func, time = int(func), int(time)
            if sta_or_end == "start":
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(func)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time+1
        return res
