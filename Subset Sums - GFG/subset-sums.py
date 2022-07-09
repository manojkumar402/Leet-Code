#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
        def rec(p, up, ans):
            if len(up) == 0:
                ans.append(p)
                return
            ch = up[0]
            rec(p+[ch], up[1:], ans)
            rec(p, up[1:], ans)
            return ans
        a = rec([], arr, [])
        ans = []
        for sub in a:
            s = sum(sub)
            ans.append(s)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends