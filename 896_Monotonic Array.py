class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2: return True
        direction = None
        for i in range(1, len(A)):
            if direction and A[i]*direction < A[i-1]*direction: return False
            if A[i] > A[i-1]: direction = 1
            elif A[i] < A[i-1]: direction = -1
        return True  
        
        # shorter one
        # if len(A) <= 2: return True
        # return all(A[i]>=A[i-1] for i in range(1, len(A))) or all (A[i]<=A[i-1] for i in range(1, len(A)))
