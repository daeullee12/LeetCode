class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """





        # TC O(logn)
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # m = (l + r) // 2  # may couse overflow in other language
            m = l + ((r - l) // 2) # avoiding overflow
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1