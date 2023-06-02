class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1 for i in range(len(nums))]
        prefix, postfix = 1, 1

        # prefix [1 1*1 1*2 2*3] postfix [12*2 4*3 1*4 1]
        for i in range(1,len(nums)):
            if i > 0:
                prefix *= nums[i-1]
                postfix *= nums[len(nums)-i]
            output[i] *= prefix
            output[len(nums)-1-i] *= postfix
        return output
