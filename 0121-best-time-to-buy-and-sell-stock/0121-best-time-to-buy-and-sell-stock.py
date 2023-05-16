class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = max(maxP, prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return maxP


        # O(n), O(1)
        # max_profit = 0
        # buy = 0

        # for sell in range(1,len(prices)):
        #     if prices[buy] > prices[sell]:
        #         buy = sell
        #     else: 
        #         max_profit = max(max_profit, prices[sell] - prices[buy])

        # return max_profit
    