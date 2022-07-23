class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        return self.solve(s,t,len(s)-1, len(t)-1)
        
    def solve(self, s,t,i,j):
        if j < 0:
            return 1
        if i < 0:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if s[i] == t[j]:
            self.dp[i][j] = self.solve(s,t,i-1,j-1) + self.solve(s,t,i-1,j)
            return self.dp[i][j]
        else:
            self.dp[i][j] = self.solve(s,t,i-1,j)
            return self.dp[i][j]