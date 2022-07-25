class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = [[[-1 for i in range(3)] for j in range(2)] for k in range(len(prices))]
        # print(self.dp)
        return self.solve(prices, 0, 1, 2)
        
    def solve(self, prices,i,buy, cap):
        if i == len(prices):
            return 0
        
        if cap == 0:
            return 0
        profit = 0
        if self.dp[i][buy][cap] != -1:
            return self.dp[i][buy][cap]
        if buy:
            profit = max(-prices[i] + self.solve(prices,i+1, 0, cap), self.solve(prices,i+1,1,cap))
        else:
            profit = max(prices[i] + self.solve(prices,i+1,1,cap-1), self.solve(prices, i+1, 0, cap))
        self.dp[i][buy][cap] = profit
        return profit