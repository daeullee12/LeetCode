class Solution:
    def rob(self, nums: List[int]) -> int:

        one, two = 0, 0

        for i in range(0, len(nums)):
            one, two = two, max(nums[i] + one, two)
        return two
