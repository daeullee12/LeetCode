class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        nset = set()
        hmap = {}
        count = 1
        
        for i in range(len(nums)):
            if nums[i] in nset:
                continue

            if nums[i] - 1 in nset:
                count += 1

            else: count = 1
            nset.add(nums[i])
            hmap[count] = nums[i]

        if hmap:
            return max(hmap.keys())
        else:
            return 0

        
        """    

        key: count
        value: nums[i] 

        """
