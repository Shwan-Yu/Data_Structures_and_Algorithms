class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # O(lg(n-k)) keep track of the interval
        l, r = 0, len(arr)-k
        while l < r:
            mid = (l+r)//2
            if x-arr[mid] > arr[mid+k]-x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]  
        
        # passed, write myself, O(lg(n)+k)
#         def bs(arr, x):
#             l, r = 0, len(arr)-1
#             while l <= r:
#                 mid = (l+r)//2
#                 val = arr[mid]
#                 if val == x: return mid
#                 elif val < x: l = mid+1
#                 else: r = mid-1
#             return l
        
#         pos = bs(arr, x)
#         l, r = pos-1, pos
#         while k > 0:
#             if l < 0:
#                 r += k
#                 break
#             elif r > len(arr)-1:
#                 l -= k
#                 break
#             if abs(arr[l]-x) <= abs(arr[r]-x): l-=1
#             else: r += 1
#             k -= 1
#         return arr[l+1:r]
