
class Solution:
    def trappingWater(self, height,n):
        #Code here
        water = []
        mLeft = []
        mRight =[0 for i in range(len(height))]
        mLeft.append(height[0])
        mRight[len(height) - 1] = height[len(height) - 1]
        for i in range(1, len(height)):
            mLeft.append(max(mLeft[i-1], height[i]))
        for j in range(len(height)-2,-1,-1):
            mRight[j] = max(mRight[j+1], height[j])
        # print(mRight)
        for i in range(len(height)):
            val = min(mLeft[i], mRight[i]) - height[i]
            water.append(val)
        return sum(water)
           


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends