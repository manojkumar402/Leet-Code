class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[None for i in range(amount+1)] for j in range(len(coins)+1)] 
        # Intialization of the matrix
        for i in range(amount+1):
            dp[0][i] = 0
        for j in range(len(coins)+1):
            dp[j][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1]<=j:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]
                 