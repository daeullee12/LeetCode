class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Hasing
        hmap = {i: None for i in range(len(nums))}

        for key in hmap:
            if key not in nums:
                return key
        
        return max(nums) + 1
        

