# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # # Your code here
        # prefix = [0]
        # for i in range(1, N):
        #     prefix.append(prefix[i-1] + A[i-1])
        # # print(prefix)
        # suffix = [0 for i in range(N)]
        # for i in range(N-2, -1, -1):
        #     suffix[i] = suffix[i+1] + A[i+1]
        # # print(suffix)
        # for i in range(N):
        #     if suffix[i] == prefix[i]:
        #         return i+1
        
        tot_sum = 0
        for val in A:
            tot_sum += val
        curr_sum = 0
        for i in range(N):
            if curr_sum == (tot_sum - curr_sum - A[i]):
                return i+1
            curr_sum += A[i]
        return -1

#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends