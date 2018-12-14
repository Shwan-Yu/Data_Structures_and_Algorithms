class Codec:
    def __init__(self):
        self.dic = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dic.values():
            h_code = hash(longUrl)
            self.dic[h_code] = longUrl
            return str(h_code)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[int(shortUrl)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
