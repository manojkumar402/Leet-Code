#User function Template for python3

class Solution:
	def characterReplacement(self, s, k):
		d={}
		i = 0 
		j = 0
		maxlength = 0
		maxfreq = 0
        while j < len(s):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            
            maxfreq = max(maxfreq, d[s[j]])
            
            if j-i+1 - maxfreq > k:
                if d[s[i]] > 1:
                    d[s[i]] -=1
                else:
                    d.pop(s[i])
                i+=1
                # remove ch from dict()
            maxlength = max(maxlength, j - i + 1)
            j +=1
            
        return maxlength
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		k = int(input())
		ob = Solution()
		ans = ob.characterReplacement(s, k)
		print(ans)

# } Driver Code Ends