class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = collections.defaultdict(int)
        for i, char in enumerate(order):
            order_map[char] = i
        words = [[order_map[char] for char in word] for word in words]
        # compare two list of int: [1, 2, 4] < [1, 2, 5]
        for i in range(1, len(words)):
            if words[i] <= words[i-1]: return False
        return True
