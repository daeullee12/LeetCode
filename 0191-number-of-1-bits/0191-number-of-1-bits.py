class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1: mod, TC O(1), SC O(1)
        # res = 0
        # while n:
        #     res += n % 2
        #     n >>= 1
        
        # return res

        # Solution 2: & TC O(1), SC O(1)
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

        