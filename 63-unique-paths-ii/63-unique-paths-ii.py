class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0
        self.dp =  [[-1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))] 
        return self.solution(obstacleGrid, 0, 0)
        
        # USE DP ---> USED ;)
        
    def solution(self, maze, row, col):
        if row == len(maze) - 1 and col == len(maze[0]) - 1 :
            return 1
        if maze[row][col] == 1:
            return 0
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