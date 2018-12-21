class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.sentence = None
        self.hot = 0
        
class AutocompleteSystem(object):
    # Trie
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.wordSearch = ""
        self.root = TrieNode()
        for sentence, time in zip(sentences, times):
            self.buildTrie(sentence, time)
    
    def buildTrie(self, sentence, time):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        node.sentence = sentence
        node.hot -= time
        
    def searchSentence(self, sentence):
        node = self.root
        for char in sentence:
            if char not in node.children: return []
            node = node.children[char]
        return self.dfsGetAll(node)
    
    def dfsGetAll(self, node):
        res = []
        if node: # dfs until node is None
            if node.isEnd: res.append((node.hot, node.sentence))
            # no else
            for key in node.children:
                res += self.dfsGetAll(node.children[key])
        return res
    
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c != "#":
            self.wordSearch += c
            res = self.searchSentence(self.wordSearch)
        else:
            self.buildTrie(self.wordSearch, 1)
            self.wordSearch = ""
        return [sentence for hot, sentence in sorted(res)[:3]] # can't reverse because ASCII code order.
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
