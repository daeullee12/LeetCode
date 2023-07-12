class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        one, two = 0, 0

        for n in nums:
            one, two = two, max(n + one, two)
        return two