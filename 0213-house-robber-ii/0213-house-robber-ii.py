class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(sublist):
            one, two = 0, 0

            for i in range(len(sublist)):
                one, two = two, max(sublist[i] + one, two)
            return two

        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))

        