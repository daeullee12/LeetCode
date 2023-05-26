class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = []

        for n in nums:
            if n not in q:
                q.append(n)
            else:
                q.remove(n)
        
        return q[0]
                
                