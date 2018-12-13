# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while True:
            buf_copy = [""] * 4
            length = read4(buf_copy)
            len_copy = min(n-index, length)
            if not len_copy: break
            for i in range(len_copy):
                buf[index] = buf_copy.pop(0)
                index += 1
        return index
