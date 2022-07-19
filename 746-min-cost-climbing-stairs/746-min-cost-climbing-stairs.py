class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [-1 for i in range(len(cost)+1)]
        return min(self.solve(cost, len(cost)-1), self.solve(cost, len(cost)-2))
    def solve(self, cost, i):
        if i == len(cost):
            return 0
        if i == 0:
            return cost[0]
        if i == 1:
            return cost[1]
        if self.dp[i] != -1:
            return self.dp[i]
        self.dp[i] = cost[i] + min(self.solve(cost,i-1), self.solve(cost, i-2))
        return self.dp[i]
        