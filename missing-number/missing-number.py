class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hmap = set(nums)
        
        for i in range(len(nums)):
            if i not in hmap:
                return i
        
        return i + 1            