class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # two pointers, be aware that don't write down 1, and count can take multiple position: 12 = "1", "2".
        tail = i = 0
        while i < len(chars):
            count = 1
            char = chars[i]
            while i+1 < len(chars) and char == chars[i+1]:
                i += 1; count += 1
            chars[tail] = char
            if count > 1:
                str_count = str(count)
                chars[tail+1: tail+1+len(str_count)] = str_count
                tail += len(str_count)
            tail += 1; i += 1
        return tail
