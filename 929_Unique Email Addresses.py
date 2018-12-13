class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        memo = set()
        for email in emails:
            loc, dom = email.split("@")
            if "+" in loc: loc = loc[:loc.index("+")]
            loc = "".join(loc.split("."))
            memo.add(loc+"@"+dom)
        return len(memo)
