class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        self.dp = [[None for i in range(len(s)+1)]for j in range(len(s)+1)]

        return self.rec(s, s[::-1], len(s), len(s))
        
    def rec(self, X, Y, n, m):
        if n == 0 or m == 0:
            return 0
        if self.dp[n][m] != None:
            return self.dp[n][m]
        else:
            if X[n-1] == Y[m-1]:
                self.dp[n][m] = 1 + self.rec(X, Y, n-1,m-1)
                return self.dp[n][m]
            else:
                self.dp[n][m] = max(self.rec(X, Y, n-1,m),self.rec(X, Y, n,m-1))
                return self.dp[n][m]