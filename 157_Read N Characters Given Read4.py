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
        i = 0
        while i < n:
            buf_copy = [""] * 4
            length = read4(buf_copy)
            if not length: break
            # if n-i < length: get n-i; else get length
            copy_length = min(n-i, length)
            buf[i:i+copy_length] = buf_copy[:copy_length]
            i += copy_length
        return i
