class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        self.dp = [-1 for i in range(len(s))]
        return self.solve(0, s) - 1
        
        
    def check(self, s, i, j):
        tmp = s[i:j+1]
        if tmp == tmp[::-1]:
            return True
        return False
    def solve(self, i, s):
        if i >= len(s):
            return 0
        if self.dp[i] != -1:
            return self.dp[i]
        maxi = float('inf')
        for j in range(i, len(s)):
            if self.check(s, i, j):
                maxi = min(maxi, 1 + self.solve(j+1, s)) 
            self.dp[i] = maxi
        return maxi
        