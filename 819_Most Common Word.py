class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        count = collections.Counter(paragraph.lower().split())
        for word, time in count.most_common():
            if word not in ban: return word
