class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1: Hasing TC O(n), SC O(n)
        # hmap = {i: None for i in range(len(nums))}

        # for n in nums:
        #     hmap.pop(n, None)

        # if hmap:
        #     return list(hmap.keys())[0]    
        # return len(nums)
        
        # Solution 2: XOR TC O(n), SC O(n)

        # missing = len(nums)
        # for i, n in enumerate(nums):
        #     missing ^= i ^ n
        # return missing

        # Solution 3: Sum
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
