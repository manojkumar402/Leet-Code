class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if grid[i][j]==1:
                return True
            if i<=0 or i>=m-1 or j<=0 or j>=n-1:
                return False
            grid[i][j]=1
            up=dfs(i-1,j)
            down=dfs(i+1,j)
            left=dfs(i,j-1)
            right=dfs(i,j+1)
            return left and right and up and down

        m,n = len(grid),len(grid[0])
        c=0
        # iterate through the grid from 1 to length of grid for rows and columns.
        # the iteration starts from 1 because if a 0 is present in the 0th column, it can't be a closed island.
        for i in range(1,m-1):
            for j in range(1,n-1):
                # if the item in the grid is 0 and it is surrounded by
                # up, down, left, right 1's then increment the count.
                if grid[i][j]==0 and dfs(i,j):
                    c+=1
        return c