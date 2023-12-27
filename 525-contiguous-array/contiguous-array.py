class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = {0 : -1}
        count = 0
        maxLen = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in hmap:
                maxLen = max(maxLen, i - hmap[count])

            else:
                hmap[count] = i

        return maxLen