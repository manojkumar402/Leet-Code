class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # print(len(grid), len(grid[0]))
        self.dp = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
        return self.solve(grid, 0,0)
    def solve(self, grid, i, j):
        if i == len(grid)-1 and j == len(grid[0]) - 1:
            return grid[i][j]
        if i >= len(grid) or j >= len(grid[0]):
            return float('inf')
        # move right
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        right = grid[i][j] + self.solve(grid, i, j+1) 
        down = grid[i][j] +  self.solve(grid, i+1, j) 
        self.dp[i][j] =  min(right, down)
        return self.dp[i][j]
        