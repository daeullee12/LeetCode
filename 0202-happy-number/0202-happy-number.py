class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        memo = []

        while True:
            if n == 1:
                return True
            if n in memo:
                return False
            else: memo.append(n)

            res = 0
            while n != 0:
                res += (n % 10) ** 2
                n //= 10        

            n = res