class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = set()

        for n in nums:
            if n not in q:
                q.add(n)
            else:
                q.remove(n)
        
        return list(q)[0]
                
                