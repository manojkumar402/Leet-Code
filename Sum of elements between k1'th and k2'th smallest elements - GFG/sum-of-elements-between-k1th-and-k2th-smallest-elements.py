#User function Template for python3
import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Your code goes here
        first = self.findKth(A, K1)
        second = self.findKth(A, K2)
        ans = 0
        i = 0
        while i < len(A):
            if A[i] > first and A[i] < second:
                ans += A[i]
            i += 1
        return ans
        # while first < second:
    def findKth(self, arr, k):
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, -1 * arr[i])
            if len(heap) == k+1:
                heapq.heappop(heap)
        return abs(heap[0])
        # while i < len(arr):
        #     if len(heap) == 0:
        #         heapq.heappush(heap, arr[i])
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        sz = [int(x) for x in input().strip().split()]
        k1, k2 = sz[0], sz[1]
        ob=Solution()
        print( ob.sumBetweenTwoKth(a, n, k1, k2) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends