class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # same as next permutation
        lst = list(str(n))
        i, j = len(lst)-1, -1
        while i > 0:
            if lst[i] > lst[i-1]:
                j = i-1
                break
            i -= 1
        for i in reversed(range(len(lst))):
            if lst[i] > lst[j]: 
                lst[i], lst[j] = lst[j], lst[i]
                lst[j+1:] = sorted(lst[j+1:])
                break
        res = int("".join(lst))
        return res if j != -1 and res.bit_length() <= 31 else -1
