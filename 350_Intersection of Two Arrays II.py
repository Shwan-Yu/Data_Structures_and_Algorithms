class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1
        return res
    
        # dic[num] = dic.get(num, 0) + 1
