class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # Solution 1: TC O(nlogn)
        # res = [0]
        # for i in range(1,n+1):
        #     count = 0
        #     while i:
        #         count += i % 2
        #         i = i // 2 
        #     res.append(count)

        # return res

        ans = [0] * (n+1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
            
        return ans

