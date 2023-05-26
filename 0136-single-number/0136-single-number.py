class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solustion 1: Hashset, TC O(n), SC O(n)
        # q = set()

        # for n in nums:
        #     if n not in q:
        #         q.add(n)
        #     else:
        #         q.remove(n)
        
        # return list(q)[0]
                
        # Solution 2: bit manipulation TC O(n), O(1)

        res = 0
        for n in nums:
            res ^= n

        return res        