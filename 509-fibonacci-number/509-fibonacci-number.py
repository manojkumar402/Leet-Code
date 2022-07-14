class Solution:
    def fib(self, n: int) -> int:
        self.dp = [-1 for i in range(n+1)]
        
        def fibo(n)->int:
            if n == 0 or n == 1:
                return n
            if self.dp[n] != -1:
                return self.dp[n]
            else:
                self.dp[n] =  fibo(n-1) + fibo(n-2)
                return self.dp[n]
        return fibo(n)