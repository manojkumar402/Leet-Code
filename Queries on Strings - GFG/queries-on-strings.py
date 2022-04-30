#User function Template for python3

class Solution:
	def SolveQueris(self, str, Query):
		# Code here
	    ans = []
	    for each in Query:
	        sub = str[(each[0]-1):each[1]]
	        ans.append(len(set(sub)))
	    
	    
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		q = int(input())
		Query = []
		for i in range(q):
			a = list(map(int, input().split()))
			Query.append(a)
		obj = Solution()
		ans = obj.SolveQueris(str, Query)
		for _ in ans:
		    print(_, end = " ")
		print()
	


# } Driver Code Ends