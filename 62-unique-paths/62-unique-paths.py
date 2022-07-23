class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0 for i in range(n)] for j in range(m)] 
        self.dp =  [[-1 for i in range(n)] for j in range(m)] 
        return self.solution(board, 0, 0)
        
        # USE DP
        
    def solution(self, maze, row, col):
        if row == len(maze) - 1 and col == len(maze[0]) - 1 :
            return 1
        count = 0
        if row < len(maze) - 1:
            #down
            if self.dp[row][col] != -1:
                count = self.dp[row][col]
            else:
                count += self.solution(maze, row + 1, col)
        if col < len(maze[0]) - 1:
            #right
            if self.dp[row][col] != -1:
                count = self.dp[row][col]
            else:
                count += self.solution(maze, row, col + 1)
        self.dp[row][col] = count
        return count