
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # solution 1: max() -> TC O(n * n)
        # while len(stones) > 1:
        #     first = stones.pop(stones.index(max(stones)))
        #     second = stones.pop(stones.index(max(stones)))
        #     print(first, second)
        #     if first != second:
        #         stones.append(abs(first-second))

        # if len(stones) == 1:
        #     return stones.pop()
        # return 0

        # solution 2: Heap -> TC O(nlogn)
        stones = [-n for n in stones] # O(nlogn)
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

    #     #solution 3: sort() -> TC O(nlogn)
    #     stones.sort()

    #    while len(stones) > 1:
           
    #         first = heapq.heappop(stones)
    #         second = heapq.heappop(stones)
    #         if first != second:
    #             heapq.heappush(stones, first - second)

    #     stones.append(0)
    #     return abs(stones[0])