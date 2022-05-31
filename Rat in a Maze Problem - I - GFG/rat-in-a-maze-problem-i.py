#User function Template for python3

class Solution:
    def findPath(self, m, n):
        if m[n-1][n-1] == 0:
            return [-1]
        return self.allPaths(m, "", 0, 0, [])
      
    def allPaths(self, maze, p, r, c, ans):
        if r == len(maze) - 1 and c == len(maze[0]) - 1:
            ans.append(p)
            return ans
        if maze[r][c] == 0:
            return ans

        maze[r][c] = 0

        if r < len(maze) - 1:
            self.allPaths(maze, p + 'D', r + 1, c, ans)
        if c < len(maze[0]) - 1:
            self.allPaths(maze, p + 'R', r, c + 1, ans)
        if r > 0:
            self.allPaths(maze, p + 'U', r - 1, c, ans)
        if c > 0:
            self.allPaths(maze, p + 'L', r, c - 1, ans)

        maze[r][c] = 1
        
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends