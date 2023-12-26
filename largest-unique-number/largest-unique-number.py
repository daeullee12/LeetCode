class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        ans = -1
        
        for n in nums:
            if counts[n] == 1:
                ans = max(ans, n)
        
        return ans