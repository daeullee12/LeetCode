class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, 0
        rain = 0

        for i in range(1, len(height) - 1):

            l = max(height[:i])
            r = max(height[i + 1:])
            rain += max(0, min(l, r) - height[i])

        return rain
            