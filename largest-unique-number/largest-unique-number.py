class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        once = set()
        more = set()
        
        for n in nums:
            if n not in once and n not in more:
                once.add(n)
            elif n in once:
                once.remove(n)
                more.add(n)
            else:
                continue
            
        return max(list(once)) if len(once) != 0 else -1