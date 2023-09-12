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
                return [i, hmap[nums[i]]]
            else:
                complement = target - nums[i]
                hmap[complement] = i

        