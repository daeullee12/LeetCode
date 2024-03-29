class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort -> O(n^2)
        
        for i in range(len(nums) - 1, 0, -1):
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
        
