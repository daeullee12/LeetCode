from heapq import *

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # solution 1: max() -> TC O(n)
        # while len(stones) > 1:
        #     first = stones.pop(stones.index(max(stones)))
        #     second = stones.pop(stones.index(max(stones)))
        #     print(first, second)
        #     if first != second:
        #         stones.append(abs(first-second))

        # if len(stones) == 1:
        #     return stones.pop()
        # return 0

        # Heapify() -> O(1)
        stones = [n * (-1) for n in stones]

        while len(stones) > 1:
            heapify(stones)
            first = heappop(stones)
            second = heappop(stones)
            if first != second:
                heappush(stones, first - second)

        if len(stones) == 1:
            return abs(heappop(stones))
        return 0