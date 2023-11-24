class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        cur, ans = 0, 0
        for i in range(len(nums)):
            cur += nums[i]
            ans = min(ans, cur)
        
        return abs(ans) + 1
            