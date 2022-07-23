class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = [[-1 for i in range(2)] for j in range(len(prices))]

        return self.solve(prices, 0, 1)
    def solve(self, prices, i, buy):
        if i == len(prices):
            return 0
        profit = 0
        if self.dp[i][buy] != -1:
            return self.dp[i][buy]
        if buy:
            profit = max(-prices[i] + self.solve(prices, i+1, 0), self.solve(prices,i+1, 1))
        else:
            profit = max(prices[i] + self.solve(prices, i+1, 1),self.solve(prices,i+1, 0))
        self.dp[i][buy] = profit
        return profit