
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
        stones = [-n for n in stones] 
        heapq.heapify(stones) # O(nlogn)

        while len(stones) > 1:
            first = heapq.heappop(stones) # O(logn)
            second = heapq.heappop(stones) # O(logn)
            if first != second:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

        # solution 3: sort() -> TC O(nlogn) * n
 
        # while len(stones) > 1:
        #     stones.sort()
        #     first = stones.pop()
        #     second = stones.pop()
        #     if first != second:
        #         stones.append(abs(first - second))

        # stones.append(0)
        # return abs(stones[0])