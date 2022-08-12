class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.visited[r][c] == 0 and grid[r][c] == '1':
                    # self.visited[r][c] = 1
                    ans += 1
                    self.solve(r, c, grid)
        return ans
    def solve(self, row, col, grid):
        if row < 0 or row >= len(grid):
            return 
        if col < 0 or col >= len(grid[0]):
            return
        if self.visited[row][col] == 1:
            return
        self.visited[row][col] = 1
        # up
        if row-1 >= 0 and grid[row-1][col] == '1':
            self.solve(row-1, col,grid)
        # down
        if row + 1 < len(grid) and grid[row+1][col] == '1':
            self.solve(row+1, col,grid)
        # left
        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.solve(row, col+1, grid)
        # right
        if col - 1 >= 0 and grid[row][col-1] == '1':
            self.solve(row, col-1,grid)