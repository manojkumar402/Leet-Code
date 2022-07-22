class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.dp = [[-1 for i in range(n+1)] for j in range(target+1)]
        
#         for i in range(n+1):
#             self.dp[0][i] = 0
#         for j in range(target+1):
#             self.dp[j][0] = 0
#         self.dp[0][0] = 1
        
#         for i in range(target+1):
#             for j in range(n+1):
#                 for l in range(1, k+1):
                   
        return self.solve(n, k , target)  % (10 ** 9 + 7)

    
    def solve(self, dice, faces, target):
        # base case
        if target < 0:
            return 0
        if dice == 0 and target != 0 :
            return 0
        if target == 0 and dice != 0:
            return 0
        if dice == 0 and target == 0:
            return 1
        if self.dp[target][dice] != -1:
            return self.dp[target][dice]
        ans = 0
        for i in range(1, faces+1):
            ans += self.solve(dice-1, faces, target - i)
            self.dp[target][dice] = ans
        return ans        
        
   