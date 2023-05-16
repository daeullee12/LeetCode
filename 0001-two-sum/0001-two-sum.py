class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution 1: brute force
        # solution 2: hash map -> O(n), O(n)

        prevMap = {}
                
        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap.keys():
                return [prevMap[diff], i]
            prevMap[n] = i
        return 
