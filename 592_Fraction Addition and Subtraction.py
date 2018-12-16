class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(i, j):
            while j: 
              i, j = j, i%j
            return i
        lst = expression.replace("+", " +").replace("-", " -").split()
        A, B = 0, 1
        for num in lst:
            a, b = num.split("/")
            a, b = int(a), int(b)
            A = A*b + B*a
            B *= b
            devisor = gcd(A, B)
            A /= devisor; B /= devisor
        return str(A) + "/" + str(B)
