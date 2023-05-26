class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Brute Fore TC O(2^n)
        # Memoization TC O(n) SC O(n)
        return self.helper(n, {})

    def helper(self, n, data):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
            
        if n in data:
            return data[n]
        data[n] = self.helper(n-1, data) + self.helper(n-2, data)
        return data[n]

        # # Dynamic Programming TC O(n) SC O(1)
        # a, b = 1, 1
        # for i in range(n):
        #     a, b = b, a + b
        # return a
