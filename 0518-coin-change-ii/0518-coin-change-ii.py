class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            newDP = dp

            for a in range(1, amount + 1):
                if a >= coins[i]:
                    newDP[a] += newDP[a - coins[i]]
            dp = newDP
        
        return dp[amount]