class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # e.g A:4,B:4,C:2 D:3, n = 3
        count = collections.Counter(tasks)
        # get the most common tasks as the base
        l = count.most_common()[0][1]
        common_tasks = [task for task, time in count.items() if time == l]
        # first have [AB],[AB],[AB],[AB] and add C, D in it to separate them, we don't add other char into the last chunk because there is no restriction n for the last chunk
        lst = [common_tasks[:] for i in range(l)]
        i = 0
        # when C, we have [ABC], [ABC], [AB], [AB]
        # when D, we have [ABC], [ABC], [ABD], [AB] then i return back to 0 and add the rest 2 Ds, which make the list [ABCD], [ABCD], [ABD], [AB]. In this way we separate all char as far as we can.
        for t in count.keys():
            if t not in common_tasks:
                for _ in range(count[t]):
                    lst[i].append(t)
                    i = (i+1)%(l-1)
        # Now we have [ABCD], [ABCD], [ABD], [AB], we just need to pick the max between n+1 and block intervals and add it to the answer, the last chunk is special so we skip it.
        # So res = 4+4+4
        res = 0
        for group in lst[:-1]:
            res += max(len(group), n+1)
        # last one don't need the additional waiting time, so we don't need to check intervals with n, just add its intervals.
        # res = 4+4+4+2 = 14
        return res+len(lst[-1])
                    
