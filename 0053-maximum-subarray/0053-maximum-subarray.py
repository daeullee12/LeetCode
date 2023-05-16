class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Kadane's Algorithm, dynamic programming
        
        for i in range(1,len(nums)):
            # nums[i] = maximum sum at index 0 to i
            nums[i] = max(nums[i], nums[i] + nums[i-1]) 

        return max(nums)
