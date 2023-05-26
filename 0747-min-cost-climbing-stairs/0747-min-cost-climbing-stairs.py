class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        def helper(i, minCost):
            if i == 0 or i == 1:
                return 0
            if i in minCost:
                return minCost[i]
            minCost[i] = min(helper(i-1,minCost) + cost[i-1], helper(i-2, minCost) + cost[i-2])
            return minCost[i]
        
        return helper(len(cost),{})

