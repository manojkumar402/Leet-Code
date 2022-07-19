class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [-1 for i in range(amount + 1)]
        ans = self.solveMem(coins, amount)
        if ans == sys.maxsize:
            return -1
        else:
            return ans
        
        
        
        
    def solveMem(self, coins, amount):
        # bc
        if amount == 0:
            return 0
        
        if amount < 0:
            return sys.maxsize
        
        if self.dp[amount] != -1:
            return self.dp[amount]
        mini = sys.maxsize
        for i in range(len(coins)):
            ans = self.solveMem(coins, amount-coins[i])
            if ans != sys.maxsize:
                mini = min(mini, 1+ans)
        self.dp[amount]= mini
        return mini
        
        
# Recursion - TLE
#     def solve(self, coins, amount):
#         # bc
#         if amount == 0:
#             return 0
#         if amount < 0:
#             return sys.maxsize
#         mini = sys.maxsize
#         for i in range(len(coins)):
#             ans = self.solve(coins, amount-coins[i])
            
#             if ans != sys.maxsize:
#                 mini = min(mini, 1+ans)
#         return mini