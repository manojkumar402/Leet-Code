class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for i in range(n)] for j in range(n)]
        return (self.solve(triangle, 0,0, len(triangle), dp))
    
    """
        2 1
        [-1]
        [2,3],
        [1,-1,-3]]
    
    """
        
    def solve(self, arr, i, j, n, dp):
        if i == n-1:
            return arr[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        first = arr[i][j] + self.solve(arr, i+1, j ,n ,dp)
        second = arr[i][j] + self.solve(arr, i+1, j+1, n, dp)
        dp[i][j] =  min(first, second)
        return min(first, second)
        
        
        