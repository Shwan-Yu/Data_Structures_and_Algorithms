class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # 1 byte: 0xxxxxxx: 0 <= < 128
        # 2 bytes: 110xxxxx: 192 <= < 224, followed by one 10xxxxxx: 128 < < 192
        # 3 bytes: 1110xxxx: 224 <= < 240, followed by two 10xxxxxx: 128 < < 192
        # 4 bytes: 11110xxx: 240 <= < 248, followed by three 10xxxxxx: 128 < < 192
        
        cnt_of_followed = 0
        for num in data:
            # this is the following sequence, so there must be count
            if 128 <= num < 192:
                if not cnt_of_followed: return False
                cnt_of_followed -= 1
            else:
                # if we didn't reduce count to 0 and meet a new starting sequence
                if cnt_of_followed: return False
                elif 0 <= num < 128: continue
                elif num < 224: cnt_of_followed += 1
                elif num < 240: cnt_of_followed += 2
                elif num < 248: cnt_of_followed += 3
                else: return False
        # if at the end we reduce count to 0 or not
        return cnt_of_followed == 0
