class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # return list(set(nums1)&set(nums2))
        
        dic = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in dic:
                res.append(num)
                del dic[num]
        return res
