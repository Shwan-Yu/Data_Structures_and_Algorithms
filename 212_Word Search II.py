# build a trie
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.isWord = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n, res = len(board), len(board[0]), []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # DFS 1. isWord; 2. normal check; 3. next TrieNode
        def dfs(board, cur, i, j, path, res):
            if cur.isWord:
                res.append(path)
                cur.isWord = False
                return
            if 0<=i<m and 0<=j<n:
                tmp = board[i][j]
                cur = cur.children.get(tmp)
                if not cur: return
                board[i][j] = "#"
                for di, dj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    dfs(board, cur, di, dj, path+tmp, res)
                board[i][j] = tmp
            
        for i in range(m):
            for j in range(n):
                dfs(board, trie.root, i, j, "", res)
        return res
