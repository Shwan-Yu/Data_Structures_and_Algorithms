class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        hex = "1234567890abcdefABCDEF"
        if IP.count(".") == 3:
            v4 = IP.split(".")
            for s in v4:
                if not s.isdigit() or str(int(s)) != s or int(s)<0 or int(s)>255: return "Neither"
            return "IPv4"
        if IP.count(":") == 7:
            v6 = IP.split(":")
            for s in v6:
                if not s or not s.isalnum() or len(s) > 4 or any(char not in hex for char in s): return "Neither"
            return "IPv6"
        return "Neither"
