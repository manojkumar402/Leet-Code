class Solution:
    def fib(self, n: int) -> int:
        # Bottom - up 
        if n <= 1:
            return n
        dp = [-1 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
        
        # Top - down Recursion + Memoization

#         self.dp = [-1 for i in range(n+1)]
        
#         def fibo(n)->int:
#             if n == 0 or n == 1:
#                 return n
#             if self.dp[n] != -1:
#                 return self.dp[n]
#             else:
#                 self.dp[n] =  fibo(n-1) + fibo(n-2)
#                 return self.dp[n]
#         return fibo(n)