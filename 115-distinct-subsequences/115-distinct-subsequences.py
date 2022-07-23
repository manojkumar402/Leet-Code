class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.dp = [[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
        return self.solve(s,t,len(s), len(t))
#         dp = [[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
#         for i in range(len(t)+1):
#             dp[0][i] = 0
#         for j in range(len(s)+1):
#             dp[j][0] = 0
#         dp[0][0] = 1
#         for each in dp:
#             print(each)
            
#         for i in range(1, len(s)+1):
#             for j in range(1, len(t)+1):
#                 if s[i-1] == t[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[-1][-1]
                    
        # intialization
        
    def solve(self, s,t,i,j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if s[i-1] == t[j-1]:
            self.dp[i][j] = self.solve(s,t,i-1,j-1) + self.solve(s,t,i-1,j)
            return self.dp[i][j]
        else:
            self.dp[i][j] = self.solve(s,t,i-1,j)
            return self.dp[i][j]