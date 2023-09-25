class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hmap = set()

        for n in nums:
            if n not in hmap:
                hmap.add(n)
            else:
                return True
        
        return False
        

        