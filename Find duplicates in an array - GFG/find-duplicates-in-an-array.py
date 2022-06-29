class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d = {}
    	res = []
        for each in arr:
            if each in d:
        	    d[each] += 1
        	else:
        	    d[each] = 1
        for key in d:
            if d[key] > 1:
                res.append(key)
        if len(res) == 0:
            return [-1]
        res.sort()
        return res


#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends