
from typing import List
class Solution:
    def findAllPossiblePaths(self, n : int, m : int, grid : List[List[int]]) -> List[List[int]]:
        def ways(i, j, n, m, grid, path, ans):
            if i >= n or j >= m:
                return
            if i == n - 1 and j == m - 1:
                path = path + [grid[i][j]]
                ans.append(path)
                return
            if i < n:
                ways(i + 1, j, n, m, grid, path + [grid[i][j]], ans)
            if j < m:
                ways(i, j + 1, n, m, grid, path + [grid[i][j]], ans)
                
            return ans
        return ways(0,0,n,m,grid,[],[])
        # return [[]]
#{ 
#  Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        grid=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findAllPossiblePaths(a[0],a[1], grid)
        
        IntMatrix().Print(res)
        

# } Driver Code Ends