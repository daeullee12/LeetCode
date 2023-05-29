class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1: mod
        res = 0
        while n:
            res += n % 2
            n >>= 1
        
        return res
        