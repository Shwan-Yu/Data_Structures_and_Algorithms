class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        # in-place
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start+=1; end-=1
        
        reverse(str, 0, len(str)-1)
        i = left = 0
        while i < len(str):
            if str[i] == " ":
                reverse(str, left, i-1)
                left = i + 1
            elif i == len(str)-1:
                reverse(str, left, i)
            i += 1
        
        # rev_word = "".join(str).split(" ")[::-1]
        # str[:] = list(" ".join(rev_word))
