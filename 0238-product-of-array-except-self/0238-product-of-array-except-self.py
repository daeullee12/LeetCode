class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # output = [1] * (len(nums))
        # prefix, postfix = 1, 1

        # for i in range(1,len(nums)):
        #     if i > 0:
        #         prefix *= nums[i-1]
        #         postfix *= nums[len(nums)-i]
        #     output[i] *= prefix
        #     output[len(nums)-1-i] *= postfix
        # return output

        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res