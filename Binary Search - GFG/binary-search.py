#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		arr.sort()
	    return self.rec(arr, 0, n-1, k)
        
        
    def rec(self, arr, st, ed, k):
        mid = int((st+ed)//2)
        if ed >= st:
            if k == arr[mid]:
                return mid
            elif k < arr[mid]:
                return self.rec(arr, st, mid-1,k)
            else:
                return self.rec(arr, mid+1, ed, k)
        else:
            return -1
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends