class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # two way, by exchange front and back
        
        # one way, O(n)
        def generateNextWords(level_of_words):
            return set(word[:i]+ch+word[i+1:] for word in level_of_words for i in range(len(word)) for ch in string.ascii_lowercase)
                    
        level, res_len = set([beginWord]), 1
        wordList = set(wordList) - level
        while level:
            if endWord in level: return res_len
            new_level = wordList & generateNextWords(level)
            res_len += 1
            wordList -= new_level
            level = new_level
        return 0
