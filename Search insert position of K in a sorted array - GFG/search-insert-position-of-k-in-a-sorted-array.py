#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        if k in Arr:
            return Arr.index(k)
        else:
            for i in range(N):
                if Arr[i] > k:
                    return i
        return N
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends