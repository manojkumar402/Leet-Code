#User function Template for python3
class Solution:

    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(n):
            X = X - A[i]
            l = 0
            r = n - 1
            while l<r:
                if l != i and r != i:
                    mid = (l + r) //2 
                    if A[l] + A[r] == X:
                        # print(A[i], A[l], A[r])
                        return 1
                    elif A[l] + A[r] < X:
                        l += 1
                    else:
                        r -= 1
                else:
                    if l== r:
                        l += 1
                    else:
                        r -= 1
            X = X + A[i]
        return 0
                    
                    
                
                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends