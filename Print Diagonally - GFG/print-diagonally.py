#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    res = []
    for i in range(N):
        r = 0
        c = i
        while r < N and c >= 0:
            res.append(A[r][c])
            r += 1
            c -= 1
    for j in range(1, N):
        r = j
        c = N - 1
    
        while r < N and c >= 0:
            res.append(A[r][c])
            r += 1
            c -= 1
    return res
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends