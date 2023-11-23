class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = 0      
        for i in range(k):
            curSum += nums[i]
        
        ans = curSum       
        left, right = 0, k - 1             
        while right < len(nums) - 1:
            print(left, right, curSum, ans)
            curSum = curSum + nums[right + 1] - nums[left]
            ans = max(ans, curSum)
            left += 1
            right += 1
            
            
        
        return ans / k
        
        