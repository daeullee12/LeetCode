class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visit = set()

        while n not in visit:
            if n == 1:
                return True
            visit.add(n)
            n = self.sumOfSquare(n)

        return False

    def sumOfSquare(self, n):
        output = 0
        
        while n:
            output += (n % 10) ** 2
            n //= 10
        
        return output