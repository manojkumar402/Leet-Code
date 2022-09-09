from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # as we are visiting nodes in level wise
        # intailly from all the nodes with 2 as value
        # we will be using BFS for this problem
        n = len(grid)
        m = len(grid[0])
        q = deque()
        # [r, c, t]
        vis = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j,0])
                    vis[i][j] = 2
                else:
                    vis[i][j] = 0
                    
        time = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        while len(q) > 0:
            r = q[0][0]
            c = q[0][1]
            t = q[0][2]
            time = max(time, t)
            q.popleft()
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and vis[nrow][ncol] != 2 and grid[nrow][ncol] == 1:
                    q.append([nrow, ncol, t+1])
                    vis[nrow][ncol] = 2
        for i in range(n):
            for j in range(m):
                if vis[i][j] != 2 and grid[i][j] == 1:
                    return -1
        return time
                
            