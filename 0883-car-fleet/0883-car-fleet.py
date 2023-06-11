class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # solution 1: stack, TC O(n) SC O(n)
        # pair = [[p, s] for p, s in zip(position, speed)]
        # stack = []

        # for p, s in sorted(pair)[::-1]:
        #     stack.append((target - p) / s)
        #     if len(stack) >= 2 and stack[-1] <= stack[-2]:
        #         stack.pop()
                
        # return len(stack)

        # Solution 2: 
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        slowest = -1
        fleet = 0

        if len(pair) == 1:
            return 1
        
        for p, s in pair:
            if (target - p) / s > slowest:
                slowest = (target - p) / s
                fleet += 1
        
        return fleet
