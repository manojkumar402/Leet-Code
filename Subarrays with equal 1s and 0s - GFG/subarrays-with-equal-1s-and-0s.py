#User function Template for python3

class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        for i in range(n):
            if arr[i] == 0:
                arr[i]= -1
        d = {}
        k = 0
        d[0] = 1
        s = 0
        count = 0
        for i in range(len(arr)):
            s += arr[i]
            if s - k in d:  # --- I
                count += d[s - k]

            # add sum to frq dict
            if s in d:
                d[s] += 1  # --- II
            else:
                d[s] = 1

        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends