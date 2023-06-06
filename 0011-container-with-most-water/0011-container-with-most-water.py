class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # TC O(n)
        res = 0

        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[r], height[l])
            res = max(res, area)

            if height[r] >= height[l]:
                l += 1

            elif height[l] > height[r]:
                r -= 1
            

        return res