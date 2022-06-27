#User function Template for python3
from collections import deque
def printFirstNegativeInteger(A, N, K):
    i = 0
    j = 0
    d = deque()
    ans = []
    while j < N:
        if A[j] < 0:
            d.append(A[j])
        if j-i+1 < K:
            j+=1
        
        elif j - i + 1 == K:
            if len(d) == 0:
                ans.append(0)
            else:
                ans.append(d[0])
                if A[i] == d[0]:
                    d.popleft()
            i+=1
            j+=1
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends