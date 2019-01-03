class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        lst = S.split()
        res = []
        for i, word in enumerate(lst):
            if word[0] in "AEIOUaeiou":
                new_word = word + "ma"
            else:
                new_word = word[1:]+word[0]+"ma"
            res.append(new_word+"a"*(i+1))
        return " ".join(res)
