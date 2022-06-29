#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, sum_): 
        A = []
        curr_sum = 0
        i = 0
        j = 0
        while j <= n:
            while curr_sum > sum_ and i < j-1:
        
                curr_sum = curr_sum - arr[i]
                i += 1
            
            if curr_sum == sum_:
                A.append(i+1)
                A.append(j)
                return A
            if j < n:
                curr_sum = curr_sum + arr[j]
            j += 1
        A.append(-1)
        return A
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends