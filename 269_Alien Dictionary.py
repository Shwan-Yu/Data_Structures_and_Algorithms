class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # get all the restrictions in order
        restrict = []
        for wA, wB in zip(words, words[1:]):
            for i in range(min(len(wA), len(wB))):
                if wA[i] != wB[i]:
                    restrict.append(wA[i]+wB[i])
                    break
        res_order = []
        chars = set("".join(words))
        while restrict:
            # while having restriction, get all first place number(number without restriction), add them to result, remove them in chars and pairs
            no_restrict = chars - set(pair[1] for pair in restrict)
            if not no_restrict: return ""
            res_order.extend(no_restrict)
            chars -= no_restrict
            restrict = [pair for pair in restrict if pair[0] not in no_restrict]
        return "".join(res_order+list(chars))
