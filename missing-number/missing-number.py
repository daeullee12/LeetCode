class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hmap = set(nums)
        
        for i in range(len(nums) + 1):
            if i not in hmap:
                return i
            