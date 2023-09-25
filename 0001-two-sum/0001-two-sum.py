class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap:
                return [hmap[nums[i]], i]
            hmap[target - nums[i]] = i 
        
    
            