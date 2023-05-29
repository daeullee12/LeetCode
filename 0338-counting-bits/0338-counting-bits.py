class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1,n+1):
            count = 0
            while i:
                count += i % 2
                i = i // 2 
            res.append(count)

        return res
