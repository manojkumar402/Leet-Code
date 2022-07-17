class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = [[None for i in range(len(text2))]for j in range(len(text1))]
        a =  self.rec(text1, text2, len(text1), len(text2))
        # print(self.dp)
        return a
    # recursion + memoization 
    def rec(self, X, Y, n, m):
        if n == 0 or m == 0:
            return 0
        if self.dp[n-1][m-1] != None:
            return self.dp[n-1][m-1]
        else:
            if X[n-1] == Y[m-1]:
                self.dp[n-1][m-1] = 1 + self.rec(X, Y, n-1,m-1)
                return self.dp[n-1][m-1]
            else:
                self.dp[n-1][m-1] = max(self.rec(X, Y, n-1,m),self.rec(X, Y, n,m-1))
                return self.dp[n-1][m-1]
        
    # recursion 
#     def rec(self, X, Y, n, m):
#         if n == 0 or m == 0:
#             return 0
        
#         if X[n-1] == Y[m-1]:
#             return 1 + self.rec(X, Y, n-1,m-1)
#         else:
#             return max(self.rec(X, Y, n-1,m),self.rec(X, Y, n,m-1))