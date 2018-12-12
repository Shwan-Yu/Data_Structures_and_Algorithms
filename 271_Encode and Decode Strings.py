class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return " ".join(str(len(s))+"-"+s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        # find the dash index, move i to the start of the next string, append this string
        res = []
        i = 0
        while i < len(s):
            dash_i = s.find("-", i)
            i = dash_i + int(s[i:dash_i]) + 1
            res.append(s[dash_i+1:i])
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
