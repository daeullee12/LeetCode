class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        answer = -1
        
        for k, v in count.items():
            if v == 1:
                answer = max(answer, k)
        
        return answer