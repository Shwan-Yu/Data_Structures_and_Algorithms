class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        par_kid = {}
        for i, parent in enumerate(ppid):
            par_kid[parent] = par_kid.get(parent,[])
            par_kid[parent].append(pid[i])
        
        res = []
        stack = [kill]
        while stack:
            cur = stack.pop()
            res.append(cur)
            stack.extend(par_kid.get(cur, []))
        return res
