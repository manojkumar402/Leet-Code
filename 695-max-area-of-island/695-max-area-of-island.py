class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.visited[r][c] == 0 and grid[r][c] == 1:
                    ans = max(ans, self.solve(r, c, grid, 0))
        return ans
    
    
    def solve(self, row, col, grid, area):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        if self.visited[row][col] == 1 or grid[row][col] == 0:
            return 0
        self.visited[row][col] = 1
        return 1 + self.solve(row-1, col,grid,area) +  self.solve(row+1, col,grid, area) + self.solve(row, col+1, grid, area) + self.solve(row, col-1,grid, area)
       