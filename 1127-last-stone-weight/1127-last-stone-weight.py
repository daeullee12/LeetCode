class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            first = stones.pop(stones.index(max(stones)))
            second = stones.pop(stones.index(max(stones)))
            print(first, second)
            if first != second:
                stones.append(abs(first-second))

        if len(stones) == 1:
            return stones.pop()
        return 0
            