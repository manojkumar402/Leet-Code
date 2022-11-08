#User function Template for python3
class Solution:
    def twoOddNum(self, arr, N):
        d = {}
        res = []
        for each in arr:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        for key in d:
            if d[key] % 2 != 0:
                res.append(key)
        res.sort(reverse = True)
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends