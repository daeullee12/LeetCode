class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        one, two = 0, 0

        for n in nums:
            one, two = two, max(n + one, two)
        return two