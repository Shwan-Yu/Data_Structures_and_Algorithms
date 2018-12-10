class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1)+len(num2))
        pos = len(product)-1
        for i, n1 in enumerate(num1[::-1]):
            cur_pos = pos
            for j, n2 in enumerate(num2[::-1]):
                product[cur_pos] += (ord(n1)-ord("0")) * (ord(n2)-ord("0"))
                product[cur_pos-1] += product[cur_pos] // 10
                product[cur_pos] %= 10
                cur_pos -= 1
            pos -= 1
        i = 0
        while len(product) > 1 and product[0] == 0: product.pop(0)
        return "".join([`char` for char in product])
