class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Hasing
        hmap = {i: None for i in range(len(nums))}

        for n in nums:
            hmap.pop(n, None)

        if hmap:
            return list(hmap.keys())[0]    
        return len(nums)
        

